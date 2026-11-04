# Monitoring & Logs

Complete visibility into every sync operation, AI call, and API interaction.

<a id="log-types"></a>

## Log Types

<a id="sync-reports"></a>

### Sync Reports

High-level summaries grouped by date and operation type with success/failure counts.

**Location:** Reports > Sync Reports

**Shows:**

- Operation type (orders, products, prices, stock, etc.)
- Date range
- Total records processed
- Success count
- Failure count
- Average duration

<a id="sync-logs-raw"></a>

### Sync Logs (Raw)

Detailed request/response data for debugging.

**Location:** Reports > Sync Logs

**Contains:**

- Full API request payload
- Full API response
- Error messages
- Stack traces
- Timestamps
- Associated records

tip

Use Sync Logs when debugging issues. The raw request/response data usually reveals the exact cause of sync failures.

<a id="real-time-notifications"></a>

### Real-time Notifications

Odoo bus notifications pushed to users when sync operations complete.

- Appears in the Odoo notification tray (top-right)
- Click to jump to the affected record
- Useful for long-running bulk operations

<a id="ai-operations-log"></a>

### AI Operations Log

All AI calls are individually logged:

- Generate (listings, content)
- Detect (product type, hijacks)
- Pricing (optimizations)
- Forecast (demand predictions)
- Reply (customer feedback responses)
- Error Fix (automated error resolution)

**Location:** Reports > AI Operations

<a id="operation-tracking"></a>

## Operation Tracking

Every sync operation records:

| Field | Description |
| --- | --- |
| **Operation Type** | Orders / Products / Prices / Stock / etc. |
| **Status** | Success / Failed / Partial |
| **Records Processed** | Total attempted |
| **Records Created** | New records in Odoo |
| **Records Updated** | Existing records modified |
| **Records Failed** | Records that errored out |
| **Duration** | Time taken |
| **Start/End Time** | Timestamps |

<a id="auto-cleanup"></a>

## Auto-cleanup

Old logs are automatically purged after a configurable number of days to keep database size manageable.

**Configure:** Amazon > Configuration > Settings > Log Retention

Default retention:

- Sync Reports: 90 days
- Sync Logs (raw): 30 days
- AI Operations: 60 days

warning

Don't set retention too low. Logs are invaluable when diagnosing issues that happened days or weeks ago. 30 days is the minimum recommended for raw logs.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Monitoring & Logs](https://docs.sdlccorp.com/docs/amazon-odoo-connector/reference/monitoring/)
