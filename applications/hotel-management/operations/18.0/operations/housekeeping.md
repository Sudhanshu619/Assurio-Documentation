# Housekeeping

Manage room cleaning, maintenance tasks, staff assignments, and lost & found items.

<a id="housekeeping-dashboard"></a>

## Housekeeping Dashboard

Access via **Dashboard > Housekeeping** or the **Housekeeping** top menu for a focused view:

- Rooms needing cleaning
- Tasks in progress
- Completed tasks today
- Staff workload

<a id="rooms-to-clean"></a>

## Rooms to Clean

![Rooms to Clean](https://docs.sdlccorp.com/assets/images/27_hk_rooms_to_clean-04b603a42dc269a215888515dae36f3e.webp)

The housekeeping view shows all rooms requiring attention, grouped by:

- **Checkout Clean** - Rooms where guests just checked out
- **Stay-Over Clean** - Daily cleaning for occupied rooms
- **Deep Clean** - Scheduled periodic thorough cleaning
- **Inspection Needed** - Cleaned rooms awaiting supervisor inspection

<a id="status-flow"></a>

### Status Flow

```
Dirty → Cleaning → Inspected → Available
```

Staff update room status as they work - the system recalculates occupancy and availability automatically.

<a id="housekeeping-tasks"></a>

## Housekeeping Tasks

Beyond room cleaning, track any hotel task.

![Housekeeping Tasks](https://docs.sdlccorp.com/assets/images/26_hk_tasks-f6a59d0fc669a8e644489ff982f3330d.webp)

<a id="activity-types"></a>

### Activity Types

Configure custom activity types like:

- Standard room cleaning
- Deep cleaning
- Bed linen change
- Towel replacement
- Minibar restocking
- Window cleaning
- Carpet cleaning
- Maintenance followup

Each type has:

- Name and sequence
- Estimated duration (hours)
- Description
- Active/inactive flag

<a id="creating-a-task"></a>

### Creating a Task

1. Navigate to **Housekeeping > Tasks** and click **New**
2. Select the room
3. Choose activity type
4. Assign to a staff member
5. Set date and scheduled time
6. Add priority (Low / Normal / High / Urgent)
7. Save and notify assigned staff

<a id="task-states"></a>

### Task States

```
New → Assigned → In Progress → Completed → Verified
                               ↘ Skipped
```

<a id="automated-task-creation"></a>

### Automated Task Creation

The system auto-creates cleaning tasks when:

- A guest checks out (checkout clean)
- Daily at midnight for occupied rooms (stay-over clean)
- On schedule for deep cleaning
- When a guest reports an issue

Configure automation via **Configuration > Scheduled Actions**.

<a id="lost-and-found"></a>

## Lost and Found

Track items left behind by guests.

![Lost and Found](https://docs.sdlccorp.com/assets/images/28_hk_lost_found-da41feb7d0dd8062cbbe76b952bb51ed.webp)

<a id="item-fields"></a>

### Item Fields

| Field | Description |
| --- | --- |
| **Item Name** | Description of found item |
| **Found Date** | When discovered |
| **Room** | Where found |
| **Found By** | Staff member who found it |
| **Category** | Clothing / Electronics / Documents / Jewelry / Other |
| **Status** | Stored / Claimed / Shipped / Disposed |
| **Photo** | Image of the item |
| **Associated Guest** | Last guest in the room (potential owner) |

<a id="workflow"></a>

### Workflow

```
Found → Stored → Contacted Guest → Claimed / Shipped / Disposed
```

<a id="features"></a>

### Features

- Auto-link to last occupant of the room
- Email notification to guest
- Shipping address capture if shipping back
- Disposal date for unclaimed items (configurable retention period)
- Photo attachment for easy identification

<a id="maintenance"></a>

## Maintenance

Track maintenance requests and work orders separately via **Operations > Maintenance**:

- HVAC repairs
- Plumbing issues
- Electrical work
- Furniture replacement
- Safety inspections

Rooms under maintenance are automatically marked unavailable to prevent bookings.

tip

Set up **Activity Types** with realistic durations so you can accurately estimate staff workload and schedule cleaning efficiently.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Housekeeping](https://docs.sdlccorp.com/docs/18.0/hotel-management/operations/housekeeping/)
