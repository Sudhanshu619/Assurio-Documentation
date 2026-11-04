# Release Notes


<a id="how-to-read-the-version-number"></a>

## How to read the version number

The Shopify Connector follows the Odoo convention `<odoo>.<major>.<minor>.<patch>` - so `v18.0.1.2` is the second patch on the first minor release of the `18.0` (Odoo 18) line.

When reporting an issue, include the exact version visible in **Apps → Shopify Connector**. It saves a round-trip.

<a id="overview"></a>

## Overview

Each release of the SDLC Shopify Odoo Connector is recorded here with a short summary of what changed. Use this page to:

- Decide whether an upgrade is worth running on your instance.
- Find the version number you're currently on (visible in **Apps → Shopify Connector**) and read what's been released since.
- Track regressions or feature additions when reporting an issue to support.

Versions follow the Odoo convention `<odoo>.<major>.<minor>.<patch>` - for example `v18.0.x`.

<a id="v180-current-release"></a>

## v18.0: Current Release

**New Features:**

- Full Odoo v18 and v19 support
- Shopify Markets support for multi-currency stores
- Enhanced webhook retry mechanism
- Net Profit Report module
- Bulk queue retry action

**Improvements:**

- Faster product import (parallel processing)
- Improved error messages in queue
- Auto-detect Shopify API rate limits and back off gracefully

**Bug Fixes:**

- Fixed variant mapping edge case with special characters
- Resolved duplicate customer creation on concurrent imports

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Release Notes](https://docs.sdlccorp.com/docs/18.0/shopify-odoo-connector/reference/release-notes/)
