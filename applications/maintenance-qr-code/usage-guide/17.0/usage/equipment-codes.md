# Equipment Codes and QR Preview

Every piece of maintenance equipment receives a unique, auto-generated code that drives QR code creation and label printing.

<a id="automatic-assignment-new-equipment"></a>

## Automatic Assignment (New Equipment)

When you create a new equipment record, the module automatically assigns an equipment code using the `maintenance.equipment.code` sequence. No action required.

![Equipment list view showing equipment with auto-assigned codes](https://docs.sdlccorp.com/assets/images/photo3-61fc6f519b3cdac6ccf750d0fedab617.webp)

<a id="manual-assignment-existing-equipment"></a>

## Manual Assignment (Existing Equipment)

For equipment that existed before the module was installed:

1. Open the equipment record from **Maintenance > Equipment**
2. Locate the **Equipment Code** field (below Serial Number)
3. Click the **Generate Code** link button next to the empty field
4. The code is assigned instantly and the QR code is generated

![Generate Code button visible for Equipment Managers when no code exists](https://docs.sdlccorp.com/assets/images/photo5-87cd18bc7e09814502dd29a9d4509893.webp)

![Equipment code successfully generated and displayed](https://docs.sdlccorp.com/assets/images/photo6-9b7e9159a152256a77d597b08b86ecf0.webp)

Manager Only

The **Generate Code** button is only visible to users in the **Equipment Manager** group. Non-manager users cannot manually generate codes.

<a id="equipment-code-sequence"></a>

## Equipment Code Sequence

Equipment codes are generated automatically using an `ir.sequence` with a yearly-resetting counter.

<a id="code-format"></a>

### Code Format

```
MEQ/%(year)s/#####
```

| Part | Description | Example |
| --- | --- | --- |
| **MEQ** | Fixed prefix (Maintenance Equipment) | `MEQ` |
| **%(year)s** | Current year (resets counter each year) | `2026` |
| **#####** | 5-digit zero-padded counter | `00001` |

<a id="example-codes"></a>

### Example Codes

- `MEQ/2026/00001` -- First equipment created in 2026
- `MEQ/2026/00042` -- 42nd equipment in 2026
- `MEQ/2027/00001` -- First equipment in 2027 (counter resets)

<a id="sequence-properties"></a>

### Sequence Properties

| Property | Value |
| --- | --- |
| **Sequence Code** | `maintenance.equipment.code` |
| **Prefix** | `MEQ/%(year)s/` |
| **Padding** | 5 digits |
| **Company** | Global (not company-specific) |
| **No Update** | True (not reset on module reinstall) |

Uniqueness Constraint

`UNIQUE(x_equipment_code)` -- "Equipment code must be unique!" Attempting to assign a duplicate code will raise a database error.

<a id="equipment-code-field-properties"></a>

## Equipment Code Field Properties

| Property | Value |
| --- | --- |
| **Field Name** | `x_equipment_code` |
| **Type** | Char (text) |
| **Readonly** | Yes (on the form view) |
| **Indexed** | Yes (for fast database lookups) |
| **Tracked** | Yes (changes logged in chatter) |
| **Copy** | No (not copied when duplicating equipment) |
| **Unique** | Yes (SQL constraint) |
| **Searchable** | Yes (added to search view) |

<a id="qr-code-preview"></a>

## QR Code Preview

Each equipment record with a code displays a live QR code preview in a dedicated tab on the form view.

<a id="qr-code-tab"></a>

### QR Code Tab

Open any equipment record and navigate to the **QR Code** tab. The tab shows:

- **QR Payload (URL)** -- The full URL encoded in the QR code, displayed as a clickable link
- **QR Code Image** -- A 220x220 pixel live QR code rendered from the payload

<a id="qr-payload-format"></a>

### QR Payload Format

The QR code encodes a direct deep-link to the equipment form:

```
<base_url>/web#id=<record_id>&model=maintenance.equipment&view_type=form
```

For example: `https://myodoo.com/web#id=42&model=maintenance.equipment&view_type=form`

<a id="computed-fields"></a>

### Computed Fields

| Field | Type | Description |
| --- | --- | --- |
| `x_qr_payload` | Char (computed) | Full URL that the QR code encodes |
| `x_qr_url` | Char (computed) | URL to Odoo's barcode endpoint that generates the QR image |
| `x_qr_image_html` | Html (computed) | HTML `<img>` tag displaying the QR code |

When QR is Generated

QR fields are computed automatically whenever the `x_equipment_code` or `company_id` changes. If no equipment code exists, all QR fields are set to empty.

<a id="scanning-qr-codes"></a>

## Scanning QR Codes

Scan printed QR labels with any mobile device to instantly access the equipment record in Odoo.

<a id="scanning-workflow"></a>

### Scanning Workflow

1. **Locate the QR label** on the physical equipment
2. **Open your camera app** or any QR scanner on your mobile device
3. **Point at the QR code** -- the device reads the encoded URL
4. **Tap the link** -- your browser opens directly to the equipment form in Odoo
5. **View or update** the equipment details, log maintenance requests, etc.

Authentication Required

The user scanning the QR code must be logged into Odoo in their browser. If not logged in, they will be redirected to the Odoo login page first, then forwarded to the equipment record after authentication.

<a id="use-cases"></a>

### Use Cases

- **Maintenance technicians** -- Scan equipment labels on the shop floor to quickly view maintenance history and log new requests
- **Inventory audits** -- Scan labels during physical inventory checks to verify equipment records
- **Onboarding** -- New team members can scan equipment to learn about each asset
- **Asset tracking** -- Track physical location by scanning labels during facility walks

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Equipment Codes and QR Preview](https://docs.sdlccorp.com/docs/17.0/maintenance-qr-code/usage/equipment-codes/)
