# Hotel Management - FAQ & Troubleshooting


<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="what-odoo-versions-are-supported"></a>

### What Odoo versions are supported?

Odoo 19 (both Community and Enterprise editions). Module version 19.0.4.0.0.

<a id="does-it-support-multiple-properties"></a>

### Does it support multiple properties?

Yes. Create as many properties as needed. Each has independent rooms, staff, rates, and reports. Consolidated dashboards show all properties together or individually.

<a id="can-i-use-it-for-hostels-or-bbs"></a>

### Can I use it for hostels or B&Bs?

Yes. While designed for hotels, it works for hostels, B&Bs, serviced apartments, vacation rentals, and any room-based hospitality business.

<a id="is-a-restaurant-pos-included"></a>

### Is a restaurant POS included?

Yes, basic restaurant functionality is included - tables, menu, KOT (Kitchen Order Tickets), and integration with guest folios. For advanced POS features (terminal, hardware), integrate with Odoo's POS module separately.

<a id="how-does-billing-work-with-taxes"></a>

### How does billing work with taxes?

Each property has default tax settings (VAT, GST, service tax). Charges automatically apply the correct tax rate based on:

- Property location
- Charge type (room, service, F&B)
- Guest nationality (for tax exemption rules)

Fully integrated with Odoo Accounting for compliance.

<a id="can-guests-book-rooms-online"></a>

### Can guests book rooms online?

Yes. The Guest Portal provides:

- Public booking portal (no login required to book)
- Guest self-service portal (manage own reservations)
- Payment integration (Stripe, PayPal, etc.)

See the [Online Booking guide](../../../guest-portal/current/portal/online-booking.md).

<a id="how-do-i-integrate-with-bookingcom--expedia"></a>

### How do I integrate with Booking.com / Expedia?

Direct OTA integration requires a third-party channel manager. The module exposes APIs for:

- Availability updates
- Rate updates
- Reservation imports

Contact SDLC Corp for implementation.

<a id="can-i-split-bills-between-multiple-guests"></a>

### Can I split bills between multiple guests?

Yes. Folios support split functionality:

- Multiple folios per reservation
- Group master folio + individual folios
- Company-paid vs guest-paid charges
- Custom line allocation

<a id="what-reports-come-out-of-the-box"></a>

### What reports come out of the box?

10+ pre-built reports:

- Daily Revenue
- Arrivals & Departures
- Booking Source
- VIP & Repeat Guests
- Occupancy
- Folio / Invoice
- Room Revenue
- Housekeeping
- KOT
- Reservation

Plus custom reports via Odoo's Pivot/Graph/Studio views.

<a id="troubleshooting"></a>

## Troubleshooting

<a id="no-room-available-when-creating-a-reservation"></a>

### "No room available" when creating a reservation

**Possible causes:**

- All rooms of the selected type are booked
- Rooms are in maintenance
- Date overlap with existing reservations
- Room status is "Out of Service"

**Solution:** Use the **Room Availability Wizard** to see which rooms are available. Check Maintenance for any out-of-service rooms.

<a id="folio-charges-not-posting-automatically"></a>

### Folio charges not posting automatically

**Checklist:**

- Is the daily room charge cron running? (Configuration > Scheduled Actions)
- Are services marked as "Completed"?
- Are KOTs closed in the restaurant?
- Check the folio for any warnings about missing tax rules

<a id="portal-booking-not-working"></a>

### Portal booking not working

**Common issues:**

1. **Property not marked "Available for Online Booking"** - Enable in property form
2. **No public rate plans** - At least one rate plan must be marked public
3. **Website module not installed** - Install the `website` module
4. **Portal URL inaccessible** - Check routing at `/hotel/booking`

<a id="dashboard-not-loading"></a>

### Dashboard not loading

**Try:**

1. Hard refresh (Ctrl+Shift+R)
2. Clear browser cache
3. Check browser console for errors
4. Verify user has Hotel User group access
5. Restart Odoo service

<a id="check-in-wizard-doesnt-show-rooms"></a>

### Check-in wizard doesn't show rooms

**Cause:** The reservation has no rooms assigned yet, or the rooms are not available.

**Solution:** On the reservation form, ensure at least one room line is added and the reservation is **Confirmed**.

<a id="staff-cant-see-reservations-from-other-properties"></a>

### Staff can't see reservations from other properties

**Cause:** Security groups restrict users to specific properties.

**Solution:** Admin can assign the **Hotel Manager** group (multi-property access) or add specific property permissions in **Configuration > Settings > Users**.

<a id="module-information"></a>

## Module Information

| Field | Value |
| --- | --- |
| **Module Name** | Hotel Management |
| **Version** | 19.0.4.0.0 |
| **Category** | Industries/Hotel |
| **License** | LGPL-3 |
| **Author** | SDLC Corp |
| **Website** | [sdlccorp.com](https://sdlccorp.com) |

<a id="support"></a>

## Support

| Channel | Details |
| --- | --- |
| **Email** | [sales@sdlccorp.com](mailto:sales@sdlccorp.com) |
| **Website** | [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Hotel Management - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/hotel-management/reference/faq/)
