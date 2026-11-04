# Assurio GitBook site-wide Git Sync — repaired layout

This folder layout matches the five GitBook site-section mappings shown in the screenshot.

| GitBook site section | Repository directory |
| --- | --- |
| Home | `./home` |
| Documentation | `./documentation` |
| API Reference | `./api-reference` |
| Changelog | `./changelog` |
| Help Center | `./help-center` |

Every section contains `README.md` and `SUMMARY.md` and `.gitbook.yaml` for GitBook's normal Markdown structure. The previous archive lacked `home/` and per-section summaries.

## How to use

1. Make a backup/branch of your GitHub repository, and check it has the Assurio pages.
2. Add the contents of this package to your GitHub repository root on the correct branch (e.g. `main`), preserving the folders. You can use GitHub Desktop to commit and push. If the existing files are already present, use the small PATCH archive to add only missing/updated configuration files.
3. In GitBook, open site-wide Git Sync → Configure. Set `Assurio-Documentation`, branch `main`, project directory `./`.
4. Ensure the mappings match the table above.
5. Press Swap direction until it says content **from GitHub will replace GitBook**, not vice versa. Then press **Sync** and check the result immediately. Do not leave/reopen the wizard before clicking Sync.
6. Look for a success/failure message in GitBook and check changes on GitHub. If it still resets, inspect Git Sync logs/error and GitHub App repository access; don't keep repeating the initial sync without knowing whether it succeeded.
7. After the GitBook editor shows Assurio's pages, set Home as the default published site section and publish the site from the GitBook dashboard.

Note: This file fixes a known folder-layout mismatch. It cannot resolve GitBook service errors, account permissions or an unpublished site. The site-level `gitbook-docs.yaml` is typically managed by GitBook during a successful site sync; don't invent or overwrite an existing one.
