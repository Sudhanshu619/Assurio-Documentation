# SDLC PSQL Query Execute

A technical utility module for Odoo 17, 18, and 19 Community Edition that allows system administrators to run PostgreSQL SELECT queries directly from the Odoo user interface, view formatted results instantly, and export data to Excel with one click.

![PSQL Query Menu Location](https://docs.sdlccorp.com/assets/images/photo1-c5f322ede476537d0987a4b7ec07fcdc.webp)

<a id="key-features"></a>

## Key Features

| Feature | Description |
| --- | --- |
| **Direct SQL Execution** | Run PostgreSQL SELECT queries directly from Odoo's interface with a single click |
| **Formatted Result Tables** | Results displayed as styled HTML tables with color-coded headers and alternating row colors |
| **XLSX Export** | One-click Excel export with company branding, report date, formatted headers, and alternating colors |
| **Save & Reuse Queries** | Save frequently-used queries with descriptive names for quick re-execution later |
| **SELECT-Only Safety** | Built-in safety guard blocks all non-SELECT queries to protect your database from modifications |
| **Chatter Integration** | Full mail thread support with messages, followers, and activities for collaboration and audit trails |

Security First

Only `SELECT` queries are permitted. The module blocks all other SQL operations (INSERT, UPDATE, DELETE, DROP, ALTER, etc.) to prevent accidental or malicious data modification. Access is restricted to system administrators only.

<a id="capabilities-overview"></a>

## Capabilities Overview

| Capability | Description |
| --- | --- |
| **Query Execution** | Execute any valid PostgreSQL SELECT statement against the Odoo database |
| **Result Rendering** | Automatic HTML table with sky-blue headers, centered text, and alternating purple row colors |
| **Scrollable Results** | Horizontal and vertical scrolling for large result sets (max 500px height) |
| **NULL Handling** | NULL values automatically displayed as `None` in results |
| **XLSX Export** | Professional Excel file with company name, report date, styled headers, and auto-fit columns |
| **Query Storage** | Save unlimited queries with names for future use |
| **Change Tracking** | Query name changes tracked via mail.thread integration |
| **Error Feedback** | Clear validation error dialogs for empty queries, non-SELECT queries, and SQL errors |

<a id="supported-versions"></a>

## Supported Versions

| Detail | Value |
| --- | --- |
| **Odoo Version** | 17.0, 18.0, 19.0 (Community Edition) |
| **Module Version** | 17.0.1.0.0 / 18.0.1.0.0 / 19.0.1.0.0 |
| **Category** | Technical |
| **License** | LGPL-3 |
| **Author** | SDLC Corp |

<a id="quick-start"></a>

## Quick Start

1. [Installation and Setup](../../getting-started/18.0/getting-started/setup.md)
2. [Creating and Executing Queries](../../usage-guide/18.0/usage/creating-queries.md)
3. [FAQ and Troubleshooting](../../reference/18.0/reference/faq.md)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [SDLC PSQL Query Execute](https://docs.sdlccorp.com/docs/18.0/psql-query-execute/intro/)
