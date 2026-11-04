"""Import SDLC's public application catalog into application/section GitBook groups.

Run with requests, beautifulsoup4, html5lib, markdownify and PyYAML installed.
HTML is cached outside the repository. Existing non-catalog groups are preserved.
"""
from __future__ import annotations
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import urljoin, urlsplit, unquote
import xml.etree.ElementTree as ET

if os.environ.get('SDLC_IMPORT_DEPS'):
    sys.path.insert(0, os.environ['SDLC_IMPORT_DEPS'])
import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://docs.sdlccorp.com/'
CACHE = Path(os.environ.get('TEMP', '/tmp')) / 'sdlc-docs-import-cache'
CACHE.mkdir(parents=True, exist_ok=True)


def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')


def canonical(url):
    parts = urlsplit(urljoin(BASE, url))
    return parts.scheme + '://' + parts.netloc + parts.path.rstrip('/') + '/'


def fetch(url):
    target = CACHE / (hashlib.sha256(url.encode()).hexdigest() + '.html')
    if target.exists():
        return target.read_bytes()
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=40)
            response.raise_for_status()
            target.write_bytes(response.content)
            return response.content
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def soup(data):
    return BeautifulSoup(data.decode('utf-8') if isinstance(data, bytes) else data, 'html5lib')


class DocConverter(MarkdownConverter):
    def convert_a(self, el, text, parent_tags):
        if el.get('id') and not el.get('href'):
            return '\n<a id="' + el['id'] + '"></a>\n'
        return super().convert_a(el, text, parent_tags)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Markdown hard breaks are unnecessary for the extracted block structure.
    text = '\n'.join(line.rstrip() for line in text.splitlines()).strip() + '\n'
    path.write_text(text, encoding='utf-8', newline='\n')


def identify(url):
    parts = urlsplit(url).path.strip('/').split('/')
    if len(parts) < 3 or parts[0] != 'docs':
        return None
    version = 'current'
    if re.fullmatch(r'\d+\.\d+', parts[1]):
        version = parts.pop(1)
    return parts[1], version, '/'.join(parts[2:])


def parse_page(url, raw):
    doc = soup(raw)
    body = doc.select_one('.theme-doc-markdown')
    if body is None:
        return None, []
    app, version, suffix = identify(url)
    nav = doc.select_one('aside')
    links = []
    section = 'Overview' if suffix == 'intro' else 'Documentation'
    order = 0
    if nav:
        top = nav.select('li.theme-doc-sidebar-item-category-level-1, li.theme-doc-sidebar-item-link-level-1')
        for index, item in enumerate(top):
            anchor = item.select_one('a.menu__link')
            if not anchor:
                continue
            urls = [canonical(a['href']) for a in item.select('a[href]')]
            links.extend(urls)
            if url in urls:
                section = anchor.get_text(' ', strip=True)
                section = re.sub(r'^[^\w]+', '', section)
                if suffix == 'intro':
                    section = 'Overview'
                order = index
        links.extend(canonical(a['href']) for a in nav.select('a[href]'))
    title = body.find('h1')
    title = title.get_text(' ', strip=True) if title else suffix.replace('/', ' / ')
    return dict(url=url, app=app, version=version, suffix=suffix, section=section,
                order=order, title=title, html=str(body)), links


def main():
    home = soup(fetch(BASE))
    apps = []
    for card in home.select('.sc-card'):
        title = card.select_one('.sc-title').get_text(' ', strip=True)
        anchor = card.select_one('.sc-title a[href]')
        url = canonical(anchor['href']) if anchor else None
        appslug = identify(url)[0] if url else slug(title)
        overview = card.select_one('.sc-overview')
        description = ''.join(str(x) for x in overview.contents if getattr(x, 'name', None) != 'ul')
        apps.append(dict(slug=appslug, title=title, url=url,
                         category=card.select_one('.sc-category').get_text(' ', strip=True),
                         description=BeautifulSoup(description, 'html.parser').get_text(' ', strip=True),
                         tags=[x.get_text(' ', strip=True) for x in card.select('.sc-chip')],
                         links=[dict(title=a.get_text(' ', strip=True), url=a['href']) for a in card.select('.sc-links a[href]')]))
    known = {app['slug'] for app in apps}
    sitemap = ET.fromstring(fetch(urljoin(BASE, 'sitemap.xml')))
    queue = {canonical(e.text) for e in sitemap.iter() if e.tag.endswith('loc') and identify(e.text) and identify(e.text)[0] in known}
    queue.update(a['url'] for a in apps if a['url'])
    pages = {}
    seen = set()
    errors = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        while queue:
            batch = sorted(queue - seen)
            queue = set()
            if not batch:
                break
            futures = {pool.submit(fetch, url): url for url in batch}
            for future in concurrent.futures.as_completed(futures):
                url = futures[future]
                seen.add(url)
                try:
                    page, links = parse_page(url, future.result())
                    if page:
                        pages[url] = page
                        for link in links:
                            ident = identify(link)
                            if urlsplit(link).netloc == urlsplit(BASE).netloc and ident and ident[0] in known and link not in seen:
                                queue.add(link)
                    else:
                        errors[url] = 'No documentation article in source response'
                except Exception as error:
                    errors[url] = str(error)
                if len(seen) % 50 == 0:
                    print(f'Fetched {len(seen)} URLs; {len(pages)} articles; {len(errors)} unavailable', flush=True)
    print(f'Discovered {len(apps)} applications and {len(pages)} source articles', flush=True)

    for page in pages.values():
        section = slug(page['section']) or 'overview'
        page['section_slug'] = section
        relative = page['suffix'] + '.md'
        page['path'] = ROOT / 'applications' / page['app'] / section / page['version'] / relative
    image_urls = set()
    # Persist the complete extraction before generating config, for auditability.
    for page in pages.values():
        body = soup(page['html'])
        for element in body.select('a.hash-link, button, script, style'):
            element.decompose()
        # Explicit original anchors keep fragment links valid after conversion.
        for heading in body.select('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]'):
            mark = body.new_tag('a', id=heading['id'])
            heading.insert_before(mark)
        for a in body.select('a[href]'):
            raw = a['href']
            absolute = urljoin(page['url'], raw)
            key = canonical(absolute)
            fragment = urlsplit(absolute).fragment
            if key in pages:
                a['href'] = Path(os.path.relpath(pages[key]['path'], page['path'].parent)).as_posix() + ('#' + fragment if fragment else '')
            elif raw.startswith('#'):
                a['href'] = raw
            else:
                a['href'] = absolute
        for img in body.select('img[src]'):
            img['src'] = urljoin(page['url'], img['src'])
            image_urls.add(img['src'])
        for pre in body.select('pre'):
            code = pre.find('code')
            if code:
                # Docusaurus line wrappers must not collapse adjacent code lines.
                lines = code.select('.token-line')
                text = '\n'.join(x.get_text() for x in lines) if lines else code.get_text()
                code.clear()
                code.append(text)
        markdown = DocConverter(heading_style='ATX', bullets='-', escape_underscores=False).convert(str(body))
        write(page['path'], markdown + f'\n\n---\n\nSource: [{page["title"]}]({page["url"]})\n')

    config_path = ROOT / 'gitbook-docs.yaml'
    config = yaml.safe_load(config_path.read_text(encoding='utf-8'))
    existing = config['site']['structure']
    retained = [g for g in existing if g.get('title', '').strip() not in {a['title'] for a in apps}]
    generated = []
    manifest = []
    for app in apps:
        records = [p for p in pages.values() if p['app'] == app['slug']]
        sections = {}
        for page in records:
            sections.setdefault(page['section_slug'], []).append(page)
        # Unpublished applications remain named, empty groups.
        if records:
            sections.setdefault('overview', [])
        old = next((g for g in existing if g.get('title', '').strip() == app['title']), None)
        group = dict(type='section-group', key=old['key'] if old else 'app-' + app['slug'], title=app['title'], icon='folder', children=[])
        for section, members in sorted(sections.items(), key=lambda x: (-1 if x[0] == 'overview' else min(p['order'] for p in x[1]), x[0])):
            label = 'Overview' if section == 'overview' else members[0]['section']
            directory = Path('applications') / app['slug'] / section
            summary = ['# Summary', '', f'* [{label}](README.md)']
            overview = [f'# {app["title"]} — {label}', '', app['description'], '', f'**Category:** {app["category"]}', '']
            if app['tags']:
                overview += ['**Topics:** ' + ', '.join(app['tags']), '']
            if members:
                overview += ['## Guides', '']
            versions = sorted({p['version'] for p in members}, key=lambda v: (v != 'current', v))
            for version in versions:
                version_label = 'Current documentation' if version == 'current' else 'Odoo ' + version
                summary += ['', '## ' + version_label, '']
                overview += ['### ' + version_label, '']
                for page in sorted((p for p in members if p['version'] == version), key=lambda p: (p['suffix'] != 'intro', p['suffix'])):
                    path = page['path'].relative_to(ROOT / directory).as_posix()
                    title = page['title'].replace('[', '').replace(']', '')
                    summary += [f'* [{title}]({path})']
                    overview += [f'- [{title}]({path})']
                overview += ['']
            overview += ['## Source', '', f'[SDLC Corp application catalog]({BASE})', '']
            overview += [f'- [{link["title"]}]({link["url"]})' for link in app['links']]
            write(ROOT / directory / 'README.md', '\n'.join(overview))
            write(ROOT / directory / 'SUMMARY.md', '\n'.join(summary))
            write(ROOT / directory / '.gitbook.yaml', 'root: ./\nstructure:\n  readme: README.md\n  summary: SUMMARY.md\n')
            key = app['slug'] + '-' + section
            space = dict(type='space', key=key + '-space', title=label, path=section, default=True, content={'directory': './' + directory.as_posix()})
            entry = dict(type='section', key=key + '-section', title=label, path=app['slug'] if section == 'overview' else key, icon='book-blank', children=[space])
            # Reuse the working DAN AI overview identities and route.
            if app['slug'] == 'dan-ai' and section == 'overview':
                entry['key'] = 'dan-ai-section'
                space['key'] = 'dan-ai-space'
                space['path'] = 'dan-ai'
            group['children'].append(entry)
        generated.append(group)
        manifest.append(dict(**app, article_count=len(records), sections=[s['title'] for s in group['children']]))
    config['site']['structure'] = retained + generated
    write(config_path, yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=120))
    report = dict(source=BASE, applications=manifest, article_count=len(pages), unavailable=errors,
                  hosted_image_count=len(image_urls), pages=[{k:v for k,v in p.items() if k not in ['html','path']} | {'file':p['path'].relative_to(ROOT).as_posix()} for p in pages.values()])
    write(ROOT / 'imports/sdlc-docs-manifest.json', json.dumps(report, ensure_ascii=False, indent=2))
    lines = ['# SDLC documentation import', '', f'Source: {BASE}', '',
             f'Imported {len(apps)} application groups and {len(pages)} source articles. Existing non-catalog groups are retained.', '',
             'Each application has its own group, with source sections beneath it. Versioned guides remain separate from current guides.', '',
             'Images use their original hosted URLs. Each imported article links to its source. Applications marked Docs soon remain named, empty groups with no sections or pages.', '',
             '| Application | Source articles | Sections |', '| --- | ---: | --- |']
    lines += [f'| {a["title"]} | {a["article_count"]} | {", ".join(a["sections"])} |' for a in manifest]
    if errors:
        lines += ['', '## Unavailable source URLs', ''] + [f'- {url}: {error}' for url,error in sorted(errors.items())]
    write(ROOT / 'imports/README.md', '\n'.join(lines))
    print(f'Generated {len(generated)} groups, {sum(len(g["children"]) for g in generated)} sections; {len(errors)} unavailable URLs', flush=True)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
