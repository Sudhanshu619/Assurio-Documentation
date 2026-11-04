"""Validate imported app coverage, GitBook routing, navigation and local links."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
config = yaml.safe_load((ROOT / 'gitbook-docs.yaml').read_text(encoding='utf-8'))
manifest = json.loads((ROOT / 'imports/sdlc-docs-manifest.json').read_text(encoding='utf-8'))
errors = []
keys = set()
section_paths = set()
covered = set()


def check_node(node):
    key = node['key']
    if key in keys:
        errors.append('Duplicate config key: ' + key)
    keys.add(key)
    if node['type'] == 'section':
        if node['path'] in section_paths:
            errors.append('Duplicate section route: ' + node['path'])
        section_paths.add(node['path'])
    if node['type'] == 'space':
        directory = ROOT / node['content']['directory']
        for name in ['README.md', 'SUMMARY.md', '.gitbook.yaml']:
            if not (directory / name).is_file():
                errors.append('Missing space file: ' + str(directory / name))
        summary = (directory / 'SUMMARY.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', summary):
            file = (directory / target).resolve()
            if not file.is_file():
                errors.append('Missing summary target: ' + str(file))
            covered.add(file)
    for child in node.get('children', []):
        check_node(child)


for group in config['site']['structure']:
    check_node(group)
names = {g['title'].strip() for g in config['site']['structure']}
for app in manifest['applications']:
    if app['title'] not in names:
        errors.append('Application missing from GitBook: ' + app['title'])
    if app['article_count'] == 0:
        group = next((g for g in config['site']['structure'] if g['title'].strip() == app['title']), None)
        if group and group.get('children'):
            errors.append('Docs soon group must be empty: ' + app['title'])
for page in manifest['pages']:
    path = ROOT / page['file']
    if path.resolve() not in covered:
        errors.append('Article missing from navigation: ' + page['file'])
    text = path.read_text(encoding='utf-8')
    if page['url'] not in text:
        errors.append('Source attribution missing: ' + page['file'])
    if len(text.strip()) < 100:
        errors.append('Unexpectedly empty article: ' + page['file'])

link_count = 0
for path in (ROOT / 'applications').rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    # Code examples can contain illustrative Markdown links; exclude fenced code.
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for raw in re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)', text):
        target = urlsplit(raw)
        if target.scheme or target.netloc or not target.path:
            continue
        link_count += 1
        destination = (path.parent / unquote(target.path)).resolve()
        if not destination.is_file():
            errors.append(f'Broken link in {path.relative_to(ROOT)}: {raw}')
    if '\ufffd' in text:
        errors.append('Unicode replacement character in ' + str(path.relative_to(ROOT)))

print(f'Applications: {len(manifest["applications"])}')
print(f'Imported source articles: {len(manifest["pages"])}')
print(f'GitBook sections (including existing content): {len(section_paths)}')
print(f'Local links checked: {link_count}')
print(f'Unavailable source URLs: {len(manifest["unavailable"])}')
print(f'Errors: {len(errors)}')
for error in errors:
    print(error)
raise SystemExit(bool(errors))
