# Guest Portal & Online Booking

Let guests book rooms directly through your website and manage their reservations online via the portal.

<a id="public-booking-portal"></a>

## Public Booking Portal

Navigate to `/hotel/booking` on your Odoo website for the public-facing booking interface.

<a id="search-availability"></a>

### Search Availability

Guests enter their criteria to find available rooms.

![Portal Book Search](https://docs.sdlccorp.com/assets/images/35_portal_book_search-7f48077328d6365f118d70e69052d5ed.webp)

Search by:

- Property (for multi-property hotels)
- Check-in and check-out dates
- Number of adults and children
- Room type preference
- Budget range

<a id="browse--book-rooms"></a>

### Browse & Book Rooms

Results show available rooms with photos, amenities, and pricing.

![Portal Book Rooms](https://docs.sdlccorp.com/assets/images/36_portal_book_rooms-9903ad78ce475d12680304bd860912a2.webp)

Each room card displays:

- Room type image
- Amenities list
- Rate per night
- Total cost for stay
- Availability confirmation
- **Book Now** button

<a id="booking-confirmation"></a>

### Booking Confirmation

After submission, guests receive an instant confirmation.

![Booking Confirmation](https://docs.sdlccorp.com/assets/images/38_booking_confirmation-8467ac8016751036782e34ba4c577a27.webp)

The confirmation includes:

- Reservation number
- Dates and room details
- Total cost
- Cancellation policy
- Email confirmation link
- Payment instructions (if pre-payment required)

<a id="guest-portal-access"></a>

## Guest Portal Access

After booking, guests can log into the portal to manage their reservations.

![My Reservations](https://docs.sdlccorp.com/assets/images/37_portal_my_reservations-b053eefdf042fddbac7808a11c0b7c16.webp)

<a id="portal-features"></a>

### Portal Features

| Feature | Description |
| --- | --- |
| **My Reservations** | View all past and upcoming bookings |
| **Reservation Details** | Check dates, rooms, pricing |
| **Modify Booking** | Request date changes (subject to policy) |
| **Cancel Booking** | Self-service cancellation (if allowed) |
| **Download Invoice** | Access folio PDFs |
| **Submit Feedback** | Post-stay feedback form |
| **Contact Hotel** | Send message to front desk |

<a id="portal-access"></a>

### Portal Access

Guests access the portal via:

- Magic link in confirmation email (no password needed)
- Portal login with email + password (if registered)
- Guest token in URL (secure, single-use)

<a id="configuring-online-booking"></a>

## Configuring Online Booking

<a id="step-1---enable-portal"></a>

### Step 1 - Enable Portal

Install the `portal` module (included as dependency).

<a id="step-2---configure-properties-for-online-booking"></a>

### Step 2 - Configure Properties for Online Booking

For each property, enable:

- **Available for Online Booking** toggle
- **Public Description** (shown to guests)
- **Photos Gallery** (main images)
- **Amenities shown** (which to highlight publicly)

<a id="step-3---configure-rate-plans-for-public"></a>

### Step 3 - Configure Rate Plans for Public

Mark rate plans as **Public** to appear on the portal. Keep corporate/OTA rates hidden.

<a id="step-4---set-cancellation-policy"></a>

### Step 4 - Set Cancellation Policy

Define the cancellation policy displayed on the portal:

- **Free cancellation until** (X hours before check-in)
- **Deposit required** (amount or percentage)
- **Non-refundable option** (with discount)

<a id="step-5---configure-email-templates"></a>

### Step 5 - Configure Email Templates

Go to **Configuration > Email Templates** to customize:

- Booking confirmation email
- Pre-arrival reminder
- Check-in instructions
- Post-stay feedback request

<a id="payment-integration"></a>

## Payment Integration

Online bookings can require upfront payment or deposit.

<a id="supported-payment-methods"></a>

### Supported Payment Methods

- Credit / Debit cards (via Odoo payment acquirers)
- PayPal
- Stripe
- Razorpay
- Bank transfer (manual confirmation)

<a id="payment-flow"></a>

### Payment Flow

1. Guest selects room and dates
2. Enters payment info
3. Payment is authorized/captured
4. Reservation moves to **Confirmed** status
5. Confirmation email sent

<a id="ota-channel-manager-integration"></a>

## OTA Channel Manager Integration

For connecting to Booking.com, Expedia, Airbnb, etc., integrate with a third-party channel manager. The module exposes APIs for:

- Room availability updates
- Rate updates
- Reservation imports
- Cancellation sync

Contact SDLC Corp for channel manager integration services.

tip

Pre-fill the guest profile with data from the booking form. When they stay again, all their info is already on file - smoother experience.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Guest Portal & Online Booking](https://docs.sdlccorp.com/docs/17.0/hotel-management/portal/online-booking/)
