# FAQ and Troubleshooting

Common questions, troubleshooting steps, and technical reference for the SDLC PSQL Query Execute module.

<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="can-i-run-insert-update-or-delete-queries"></a>

### Can I run INSERT, UPDATE, or DELETE queries?

No. The module only allows `SELECT` queries. All other SQL operations are blocked by a built-in safety guard. If you attempt a non-SELECT query, you will receive a validation error: *"Only SELECT queries are allowed for safety reasons."*

<a id="who-can-access-this-module"></a>

### Who can access this module?

Only users with the **Settings / System Administrator** role (`base.group_system`) can access the module. Regular users will not see the menu item or be able to access query records.

<a id="do-i-need-developer-mode-enabled"></a>

### Do I need Developer Mode enabled?

Yes. The **PSQL Query** menu is located under **Settings > Technical**, which is only visible when Developer Mode is activated. Go to **Settings > General Settings > Developer Tools > Activate Developer Mode**.

<a id="why-is-my-xlsx-export-not-working"></a>

### Why is my XLSX export not working?

The XLSX export feature requires the `xlsxwriter` Python library. Install it with:

```
pip install xlsxwriter
```

Without this library, query execution and result display will work normally, but the **XLSX** button will not function.

<a id="can-i-use-joins-subqueries-and-other-complex-sql"></a>

### Can I use JOINs, subqueries, and other complex SQL?

Yes. Any valid PostgreSQL SELECT statement is supported, including JOINs, subqueries, CTEs (WITH clauses), aggregate functions, window functions, and more. The only restriction is that the query must begin with `SELECT`.

<a id="is-there-a-limit-on-result-size"></a>

### Is there a limit on result size?

There is no hard limit on the number of rows returned. However, very large result sets may be slow to render in the browser. The result container scrolls vertically at a maximum height of **500px**. It is recommended to use `LIMIT` in your queries.

<a id="what-happens-to-null-values"></a>

### What happens to NULL values?

NULL values are automatically displayed as the string `None` in both the HTML result table and the XLSX export.

---


<a id="troubleshooting"></a>

## Troubleshooting

<a id="please-enter-a-sql-query"></a>

### "Please enter a SQL query."

**Cause:** The query field is empty or contains only whitespace.

**Solution:** Enter a valid SELECT statement in the query field before clicking **Execute/Refresh**.

<a id="only-select-queries-are-allowed-for-safety-reasons"></a>

### "Only SELECT queries are allowed for safety reasons."

**Cause:** The query does not start with `SELECT` (after stripping whitespace).

**Solution:** Ensure your query begins with `SELECT`. Remove any leading comments or statements before the SELECT keyword.

<a id="query-execution-error-relation-does-not-exist"></a>

### "Query execution error: relation does not exist"

**Cause:** The table name specified in the query does not exist in the database.

**Solution:** Verify the table name. You can find all available table names by running:

```
SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename;
```

<a id="query-execution-error-column-does-not-exist"></a>

### "Query execution error: column does not exist"

**Cause:** A column name specified in the query does not exist in the referenced table.

**Solution:** Check the column names for the table by running:

```
SELECT column_name FROM information_schema.columns
WHERE table_name = 'your_table_name'
ORDER BY ordinal_position;
```

<a id="xlsx-button-download-fails"></a>

### XLSX button download fails

**Cause:** The query record was missing, or no results have been generated yet (column_names is empty).

**Solution:** Execute the query first using the **Execute/Refresh** button, then click **XLSX**.

<a id="menu-item-not-visible"></a>

### Menu item not visible

**Cause:** Developer Mode is not enabled, or the current user does not have System Administrator access.

**Solution:**

1. Enable Developer Mode: **Settings > General Settings > Developer Tools > Activate Developer Mode**
2. Ensure your user has the **Settings / System Administrator** role

---


<a id="data-model-reference"></a>

## Data Model Reference

<a id="psqlquery"></a>

### psql.query

Main and only model in the module. Inherits from `mail.thread` and `mail.activity.mixin`.

| Field | Type | Properties | Description |
| --- | --- | --- | --- |
| `name` | Char | required, tracking=True | Query name / label for identifying saved queries |
| `query` | Text | -- | The SQL SELECT statement to execute |
| `result` | Html | readonly | Rendered HTML table of query results |
| `column_names` | Text | readonly | JSON-encoded list of column header names |
| `row_data` | Text | readonly | JSON-encoded list of data row arrays |

<a id="methods"></a>

### Methods

<a id="action_execute_queryself"></a>

#### `action_execute_query(self)`

Executes the SQL query and populates the result, column_names, and row_data fields.

| Aspect | Detail |
| --- | --- |
| **Trigger** | Execute/Refresh button (`type="object"`) |
| **Multi-record** | Yes -- iterates with `for rec in self` |
| **Validation** | Checks for empty query and non-SELECT statements |
| **Execution** | `self.env.cr.execute(query)` -- direct cursor access |
| **Column extraction** | `[desc[0] for desc in self.env.cr.description]` |
| **Data fetch** | `self.env.cr.fetchall()` |
| **Error handling** | `try/except Exception` -> `ValidationError` |

<a id="action_download_xlsxself"></a>

#### `action_download_xlsx(self)`

Triggers the XLSX file download via a URL action.

| Aspect | Detail |
| --- | --- |
| **Trigger** | XLSX button (`type="object"`) |
| **Multi-record** | No -- uses `ensure_one()` |
| **Validation** | Checks that column_names and row_data are not empty |
| **Return** | `ir.actions.act_url` pointing to `/psql_query/download_xlsx/<id>`, target: new tab |

<a id="controller-api"></a>

### Controller API

| Property | Value |
| --- | --- |
| **URL Pattern** | `/psql_query/download_xlsx/<int:record_id>` |
| **HTTP Method** | GET |
| **Authentication** | `auth='user'` -- requires authenticated Odoo session |
| **Response Type** | File download (binary XLSX) |
| **Content-Type** | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |

---


<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Website** | [sdlccorp.com](https://sdlccorp.com) |
| **Contact** | [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) |
| **Email** | [sales@sdlccorp.com](mailto:sales@sdlccorp.com) |
| **Module Name** | sdlc_psql_query_execute |
| **License** | LGPL-3 |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [FAQ and Troubleshooting](https://docs.sdlccorp.com/docs/19.0/psql-query-execute/reference/faq/)
