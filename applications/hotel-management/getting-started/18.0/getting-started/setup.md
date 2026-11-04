# Hotel Management - Installation and Setup


<a id="prerequisites"></a>

## Prerequisites

- Odoo 19 (Community or Enterprise)
- The following modules are required as dependencies and install automatically:
  - `mail` - Tracking and messaging
  - `account` - Folios and invoicing
  - `contacts` - Guest profiles
  - `portal` - Public booking portal

<a id="installation"></a>

## Installation

<a id="step-1---install-the-module"></a>

### Step 1 - Install the Module

Go to **Apps** and search for "Hotel Management". Click **Install**.

![Install Hotel Management](https://docs.sdlccorp.com/assets/images/01_apps_install-3ffdc0b1f430411d0a1d330b361de135.webp)

tip

If the module doesn't appear, enable developer mode and click **Update Apps List** first.

<a id="step-2---access-the-hotel-menus"></a>

### Step 2 - Access the Hotel Menus

After installation, the **Hotel** top-level menu appears with all submenus:

![Topbar Menus](https://docs.sdlccorp.com/assets/images/02_topbar_menus-4ceede7c8fb6ff8bd9536a99d0e8df38.webp)

Main menus include:

- **Dashboard** - Role-based views (All / Front Desk / Housekeeping / Owner / Analytics)
- **Front Desk** - Reservations, check-in, check-out, calendar
- **Rooms** - Room configuration, room types, amenities, rate plans
- **Properties** - Multi-property management
- **Housekeeping** - Tasks, room cleaning, lost & found
- **Pricing** - Rate plans, minibar items
- **Operations** - Maintenance, notifications, restaurant, transport
- **Reporting** - Revenue, occupancy, VIP, booking source reports
- **Configuration** - Settings, sequences, security groups

<a id="step-3---configure-your-first-property"></a>

### Step 3 - Configure Your First Property

See the [Property Configuration guide](../../../reservations/18.0/reservations/create-reservation.md) for adding properties, rooms, room types, and amenities.

<a id="step-4---set-up-security-groups"></a>

### Step 4 - Set Up Security Groups

Navigate to **Configuration > Settings** to configure role-based access:

![Security Groups](https://docs.sdlccorp.com/assets/images/40_role_groups_settings-3b893df11881f34fbbc9066788d97a30.webp)

Roles available:

| Role | Access Level |
| --- | --- |
| **Hotel User** | View dashboards, create reservations |
| **Front Desk** | Check-in/out, folio management |
| **Housekeeping** | Manage rooms and tasks |
| **Manager** | Full access to all properties and reports |
| **Administrator** | Configuration, settings, security |

<a id="step-5---enable-multi-property-optional"></a>

### Step 5 - Enable Multi-Property (Optional)

If you operate multiple properties, use the property picker to switch between them:

![Property Picker](https://docs.sdlccorp.com/assets/images/39_property_picker_open-7c99c73da10b0f9f5d957ab62e576eff.webp)

Each property has its own rooms, staff, and reports.

<a id="demo-data"></a>

## Demo Data

The module includes optional demo data with sample properties, rooms, guests, and reservations. This helps you explore features before going live.

To load demo data, install the module in a test database with demo data enabled.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Hotel Management - Installation and Setup](https://docs.sdlccorp.com/docs/18.0/hotel-management/getting-started/setup/)
