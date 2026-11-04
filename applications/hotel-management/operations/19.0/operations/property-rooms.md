# Properties & Rooms

Multi-property support with full room configuration including floors, types, amenities, and pricing.

<a id="properties"></a>

## Properties

Navigate to **Properties > All Properties** to see all your hotels.

![Properties Kanban](https://docs.sdlccorp.com/assets/images/24_properties_kanban-61aba097705f9bebdf506ceaab2982de.webp)

<a id="property-form"></a>

### Property Form

![Property Form](https://docs.sdlccorp.com/assets/images/25_property_form-272b62f80880b5064faea6723f7216c3.webp)

<a id="core-fields"></a>

#### Core Fields

| Field | Description |
| --- | --- |
| **Name** | Property name (shown in dashboards and reports) |
| **Code** | Short code (e.g., "NYC-PLAZA") |
| **Address** | Full property address |
| **Phone / Email** | Contact info |
| **Website** | Property website URL |
| **Check-in Time** | Default check-in hour |
| **Check-out Time** | Default check-out hour |
| **Currency** | Property base currency |
| **Timezone** | Local timezone for scheduling |
| **Tax Settings** | Default tax rules for this property |

<a id="multi-property-operations"></a>

### Multi-Property Operations

- Each property has independent rooms, staff, rates
- Users can be restricted to specific properties via security groups
- Consolidated dashboards show data across all properties
- Switch between properties using the property picker

<a id="room-types"></a>

## Room Types

Define room categories with standard features and base rates.

<a id="examples-of-room-types"></a>

### Examples of Room Types

| Type | Typical Features |
| --- | --- |
| **Standard** | 1 bed, city view, basic amenities |
| **Deluxe** | 1 king bed, premium view, enhanced amenities |
| **Junior Suite** | Separate sitting area, king bed |
| **Executive Suite** | Full suite with kitchenette |
| **Presidential Suite** | Luxury suite with multiple rooms |
| **Family Room** | Multiple beds for families |
| **Connecting Rooms** | Linked for group stays |

<a id="configuration-fields"></a>

### Configuration Fields

- Name, code, sequence
- Default capacity (adults + children)
- Default rate per night
- Default amenities
- Image gallery

<a id="amenities"></a>

## Amenities

Track room features and facilities:

- WiFi
- Air Conditioning
- Mini Bar
- Room Service
- Balcony
- Ocean View
- Kitchenette
- Jacuzzi
- Smoking / Non-smoking
- Pet-friendly
- Accessible (ADA-compliant)

Assign amenities to rooms individually or to room types as defaults.

<a id="rooms"></a>

## Rooms

Each physical room in the property is configured individually.

<a id="room-fields"></a>

### Room Fields

| Field | Description |
| --- | --- |
| **Room Number** | Unique room number (101, 202, etc.) |
| **Property** | Which property this room belongs to |
| **Floor** | Floor number (integrated with `hotel.floor` model) |
| **Room Type** | Standard / Deluxe / Suite / etc. |
| **Amenities** | Specific amenities for this room |
| **Status** | Available / Occupied / Cleaning / Maintenance |
| **Housekeeping Status** | Clean / Dirty / Inspected |

<a id="room-states"></a>

### Room States

Rooms go through multiple state changes:

```
Available → Reserved → Occupied → Dirty → Cleaning → Inspected → Available
```

<a id="floors"></a>

## Floors

For multi-floor properties, configure floors separately:

- Floor name / number
- Floor plan image (optional)
- Associated rooms
- Housekeeping zones

Useful for:

- Grouping rooms by floor for housekeeping
- Floor-specific reports
- Staff zone assignments

<a id="rate-plans"></a>

## Rate Plans

Define dynamic pricing strategies.

![Rate Plans](https://docs.sdlccorp.com/assets/images/29_rate_plans-0818d77f4d28cf0ea618a2979f803332.webp)

<a id="rate-plan-types"></a>

### Rate Plan Types

| Type | Use Case |
| --- | --- |
| **Rack Rate** | Standard published price |
| **Corporate Rate** | Negotiated rates for companies |
| **OTA Rate** | Rates for online travel agencies |
| **Promotional** | Time-limited discounts |
| **Group Rate** | Discounted rates for groups |
| **Member Rate** | Loyalty program rates |

<a id="configuration"></a>

### Configuration

- Start/end dates
- Applicable room types
- Discount percentage or fixed amount
- Minimum stay requirements
- Cancellation policy
- Meal inclusions (breakfast, half-board, full-board)

<a id="minibar-items"></a>

## Minibar Items

Configure consumable minibar items with per-unit pricing.

![Minibar Items](https://docs.sdlccorp.com/assets/images/30_minibar_items-a5c9899bc2987041edeed97f432f94bf.webp)

- Item name and description
- Unit price
- Cost price (for margin reports)
- Category (beverages, snacks, premium)
- Stock tracking (optional)

At checkout, mark consumed items to auto-post charges to the guest folio.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Properties & Rooms](https://docs.sdlccorp.com/docs/19.0/hotel-management/operations/property-rooms/)
