# Creating Reservations

Manage the complete booking lifecycle from initial inquiry to checkout.

<a id="reservation-lifecycle"></a>

## Reservation Lifecycle

```
Draft → Confirmed → Checked In → Checked Out → Done
                                            ↘ No Show / Cancelled
```

| Status | Meaning |
| --- | --- |
| **Draft** | Initial booking, not yet confirmed |
| **Confirmed** | Confirmed booking (deposit received or guaranteed) |
| **Checked In** | Guest has arrived and checked in |
| **Checked Out** | Guest has departed |
| **Done** | Folio settled, reservation closed |
| **No Show** | Guest failed to arrive |
| **Cancelled** | Cancelled by guest or hotel |

<a id="reservations-list"></a>

## Reservations List

Navigate to **Front Desk > Reservations** to see all bookings in list or kanban view.

![Reservations List Kanban](https://docs.sdlccorp.com/assets/images/16_reservations_list_kanban-149b48e34699886f005b0cc0ca92b435.webp)

<a id="views-available"></a>

### Views Available

- **Kanban** - Group by status for quick workflow visualization
- **List** - Detailed tabular view
- **Calendar** - See reservations on a calendar
- **Form** - Individual reservation details

<a id="filters"></a>

### Filters

- By property, room type, status
- Date range (check-in / check-out)
- Guest name or booking source
- VIP status

<a id="creating-a-reservation"></a>

## Creating a Reservation

<a id="step-1---open-the-reservation-form"></a>

### Step 1 - Open the Reservation Form

Click **New** from **Front Desk > Reservations** or from the calendar.

![Reservation Form](https://docs.sdlccorp.com/assets/images/17_reservations_form-1b0e23d3f9cb84d8ebd5ff1cc1c6c603.webp)

<a id="step-2---fill-required-fields"></a>

### Step 2 - Fill Required Fields

| Field | Description |
| --- | --- |
| **Guest** | Select existing guest or create new |
| **Property** | Which property for multi-property |
| **Check-in Date** | Arrival date |
| **Check-out Date** | Departure date |
| **Rooms** | Add room lines with room type and rate |
| **Adults / Children** | Guest count |
| **Booking Source** | Direct, OTA, Walk-in, etc. |
| **Rate Plan** | Select applicable pricing |
| **Special Requests** | Notes for front desk / housekeeping |

<a id="step-3---configure-room-lines"></a>

### Step 3 - Configure Room Lines

Add one or more rooms to the reservation:

- Room Type (Standard, Deluxe, Suite, etc.)
- Specific Room (optional - can be assigned at check-in)
- Rate per night
- Adults and children per room
- Extra bed requirements

<a id="step-4---confirm-the-reservation"></a>

### Step 4 - Confirm the Reservation

Click **Confirm** to move from Draft → Confirmed status. This:

- Reserves the room in the system
- Sends a confirmation email (if mail template enabled)
- Creates an initial folio draft

<a id="check-in-process"></a>

## Check-In Process

When the guest arrives:

1. Open the reservation
2. Click **Check In** button
3. The **Check-In Wizard** opens for ID verification and room assignment
4. Confirm room number
5. Collect deposit / advance payment
6. Status changes to **Checked In**

<a id="check-out-process"></a>

## Check-Out Process

On departure day:

1. Open the reservation
2. Click **Check Out** button
3. The **Check-Out Wizard** opens
4. Review folio charges (room, services, minibar, taxes)
5. Process final payment
6. Generate invoice
7. Status changes to **Checked Out** → **Done**

<a id="available-wizards"></a>

## Available Wizards

The module includes several wizards to streamline operations:

| Wizard | Purpose |
| --- | --- |
| **Check-In Wizard** | Guest arrival process with ID capture |
| **Check-Out Wizard** | Settle folio and generate invoice |
| **Extend Stay Wizard** | Change departure date mid-stay |
| **Room Exchange Wizard** | Move guest to a different room |
| **Room Availability Wizard** | Check availability for date range |
| **Notification Wizard** | Send custom email/SMS to guest |

tip

Use the **Room Availability Wizard** to quickly find available rooms for a date range without leaving the reservation form.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Creating Reservations](https://docs.sdlccorp.com/docs/19.0/hotel-management/reservations/create-reservation/)
