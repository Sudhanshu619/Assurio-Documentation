# Premium Backend Theme - Getting Started

This guide walks you through the complete installation of the SDLC Corp Premium Backend Theme for Odoo 19.

<a id="prerequisites"></a>

## Prerequisites

- A working **Odoo 19 instance** (Community or Enterprise)
- **Administrator access** to Odoo
- Developer Mode activated (recommended)

<a id="installation-steps"></a>

## Installation Steps

<a id="step-1-download-the-module"></a>

### Step 1: Download the Module

1. Visit the [Odoo App Store](https://apps.odoo.com/) and search for **SDLC Corp Premium Backend Theme**
2. Click **Buy** or **Try** (for evaluation)
3. Download the zip file

<a id="step-2-upload-to-odoo"></a>

### Step 2: Upload to Odoo

1. Go to **Settings > Technical > Update Apps List**
2. Navigate to **Apps** and search for "SDLC Theme"
3. Click **Install** on the SDLC Corp Premium Backend Theme module

![Install the Theme Module](https://docs.sdlccorp.com/assets/images/02-apps-sdlc-theme-ce46e441e9c052cfdbe5db4828249c72.webp)

tip

Alternatively, place the `sdlc_theme` folder in your Odoo addons directory, restart the service, then install from Apps.

<a id="step-3-verify-installation"></a>

### Step 3: Verify Installation

After installation:

- The Odoo backend immediately switches to the new theme layout
- A **dark sidebar** with colored app icons replaces the default top navigation
- A **top bar** displays a greeting, company switcher, and action buttons
- A **gear icon** appears in the top bar for Quick Settings access (if enabled for your user)

![Theme Applied - Dashboard](https://docs.sdlccorp.com/assets/images/01-theme-dashboard-overview-713e86c3d244d627ac8b86742d947e75.webp)

<a id="first-time-admin-configuration"></a>

## First-Time Admin Configuration

After installing, configure the global defaults that apply to all users:

1. Go to **Settings** and click **SDLC Theme** in the left menu
2. Set the system-wide defaults:

![Admin Theme Settings](https://docs.sdlccorp.com/assets/images/03-settings-sdlc-theme-fc58b441c47ca13f7e43fc1c5ac84dc3.webp)

| Setting | Options | Default |
| --- | --- | --- |
| **Default Layout Mode** | Vertical, Mini | Vertical |
| **Default Color Palette** | 12 palettes | SDLC Blue |
| **Default Font** | 13 Google Fonts | Inter |
| **Default Dark Mode** | Light, Dark, Auto | Light |
| **Default UI Style** | Flat, Glass, Neumorphism | Flat |

3. Under **Settings Access**, select which users can access the Quick Settings panel to customize their own theme

![Theme Access Settings](https://docs.sdlccorp.com/assets/images/33-theme-access-setting-a82762b8c7a668e14de5a5f1a132ecbf.webp)

info

Users without Settings Access will see the global defaults you configure here. Only users you explicitly grant access to will see the gear icon for personal customization.

<a id="user-experience-by-role"></a>

## User Experience by Role

| User Type | What They See |
| --- | --- |
| **Admin** | Full control: global defaults + personal Quick Settings |
| **User with Settings Access** | Gear icon visible: 80+ personal customizations via Quick Settings |
| **Regular User** | Global defaults applied: clean, polished theme with no customization UI |

<a id="next-steps"></a>

## Next Steps

- [Configure admin defaults in detail >](../../../admin/current/admin/admin-settings.md)
- [Customize colors & dark mode >](../../../customization/current/customization/colors-dark-mode.md)
- [Configure layout & typography >](../../../customization/current/customization/layout-typography.md)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Premium Backend Theme - Getting Started](https://docs.sdlccorp.com/docs/odoo-premium-backend-theme/installation/getting-started/)
