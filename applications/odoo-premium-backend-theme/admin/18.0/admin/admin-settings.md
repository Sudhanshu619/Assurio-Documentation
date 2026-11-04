# Admin Settings & Access Control

As an administrator, you control the default theme settings for all users and decide who gets access to personal customization.

<a id="accessing-admin-settings"></a>

## Accessing Admin Settings

Navigate to **Settings** and click **SDLC Theme** in the left menu.

![Admin Theme Settings](https://docs.sdlccorp.com/assets/images/33-theme-access-setting-a82762b8c7a668e14de5a5f1a132ecbf.webp)

<a id="theme-defaults"></a>

## Theme Defaults

These defaults apply to **all users** unless they have Settings Access and customize their own:

| Setting | Options | Default | Description |
| --- | --- | --- | --- |
| **Default Layout Mode** | Vertical, Mini | Vertical | Sidebar style for all users |
| **Default Color Palette** | 12 presets | SDLC Blue | Brand color across the UI |
| **Default Font** | 13 Google Fonts | Inter | Typography for all text |
| **Default Dark Mode** | Light, Dark, Auto | Light | Background appearance |
| **Default UI Style** | Flat, Glass, Neumorphism | Flat | Surface and shadow treatment |

![Theme Defaults Configuration](https://docs.sdlccorp.com/assets/images/03-settings-sdlc-theme-fc58b441c47ca13f7e43fc1c5ac84dc3.webp)

<a id="settings-access-control"></a>

## Settings Access Control

The **Theme Settings Users** field controls which users see the Quick Settings gear icon in the top bar.

- **Users with access**: see the gear icon, can customize 80+ personal settings
- **Users without access**: see only the global defaults you configure above

To grant access:

1. In the **Settings Access** section, toggle **Theme Settings Users**
2. Add users to the list using the tag selector
3. Click **Save**

tip

Grant Settings Access to team leads or power users who want to personalize their workspace. Keep it disabled for users who prefer a consistent, uniform experience.

<a id="how-settings-cascade"></a>

## How Settings Cascade

```
Admin Defaults (Settings > SDLC Theme)
    |
    v
User opens Odoo --> Loads admin defaults
    |
    v
Has Settings Access? --> YES --> Can customize via Quick Settings (overrides defaults)
                     --> NO  --> Uses admin defaults only
```

<a id="quick-settings-panel"></a>

## Quick Settings Panel

Users with Settings Access see a **gear icon** in the top bar. Clicking it (or pressing **Alt+T**) opens the Quick Settings panel:

![Quick Settings Panel](https://docs.sdlccorp.com/assets/images/04-quick-settings-full-9e4fd83af92fa2b2ae05f213cf6da071.webp)

The panel provides access to:

- Color palette selection
- Dark mode toggle
- Typography settings
- UI style selection
- Component styles
- View preferences
- Theme export/import/reset

Each section is covered in detail in the [Colors & Dark Mode](../../../customization/18.0/customization/colors-dark-mode.md) and [Layout & Typography](../../../customization/18.0/customization/layout-typography.md) guides.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Admin Settings & Access Control](https://docs.sdlccorp.com/docs/18.0/odoo-premium-backend-theme/admin/admin-settings/)
