# HRMS Dashboard - Installation & Setup

This guide walks you through the complete installation and setup of the SDLC Corp HRMS Employee Dashboard module for Odoo.

<a id="prerequisites"></a>

## Prerequisites

Before installing, ensure you have:

- A working **Odoo instance** (v17.0, v18.0, or v19.0 Community)
- **Administrator access** to your Odoo instance
- The following Odoo modules installed: **HR**, **HR Attendance**, **HR Holidays** (Time Off), **Project**
- **Developer Mode** enabled (for manual installation)
- Employee records created for users who will access the dashboard

<a id="dependencies"></a>

## Dependencies

The module depends on the following Odoo modules, which are installed automatically:

| Module | Technical Name | Purpose |
| --- | --- | --- |
| **Base** | `base` | Core Odoo framework (users, groups, access rights) |
| **Employees** | `hr` | Employee records, departments, and the employee form |
| **Attendances** | `hr_attendance` | Attendance records (check-in/check-out data) |
| **Time Off** | `hr_holidays` | Leave types, leave requests, allocations, and public holidays |
| **Project** | `project` | Project and task data for the Projects panel |

<a id="install-the-module"></a>

## Install the Module

<a id="step-1-download-the-module"></a>

### Step 1: Download the Module

Download the `sdlc_emp_dashboard` module package from the [SDLC Corp website](https://sdlccorp.com/) or the [Odoo App Store](https://apps.odoo.com/).

<a id="step-2-upload-to-odoo"></a>

### Step 2: Upload to Odoo

Place the module folder into your Odoo `addons` directory. The path is typically `/odoo/addons/` or a custom addons path configured in your `odoo.conf`.

<a id="step-3-update-apps-list"></a>

### Step 3: Update Apps List

Go to the **Apps** menu in Odoo, click **Update Apps List** (requires Developer Mode). Confirm when prompted.

<a id="step-4-install"></a>

### Step 4: Install

Search for **"HRMS Dashboard"** in the Apps list and click **Install**. Odoo will automatically install all required dependencies (`hr`, `hr_attendance`, `hr_holidays`, `project`).

Odoo.sh Users

If you are using Odoo.sh, you can simply add the module to your GitHub repository and it will be detected automatically. Push to a staging branch first to test before deploying to production.

<a id="link-employee-to-user"></a>

## Link Employee to User

Each user who needs to access the dashboard must have their Odoo user account linked to an employee record. This **must be done by an Administrator** before the user can use the dashboard.

<a id="step-1-open-the-employee-form"></a>

### Step 1: Open the Employee Form

Login as **Admin**. Go to **Employees > Employees** and open the employee record for the user (e.g., Marc Demo).

<a id="step-2-go-to-hr-settings-tab"></a>

### Step 2: Go to HR Settings Tab

In the employee form, click on the **HR Settings** tab (or **Work Information** tab depending on your Odoo version).

<a id="step-3-set-the-related-user"></a>

### Step 3: Set the Related User

Find the **Related User** (or **User**) field and select the Odoo user account that corresponds to this employee.

<a id="step-4-save"></a>

### Step 4: Save

Click **Save**. The employee is now linked to the user account. The dashboard will recognize this user automatically.

warning

If the user opens the dashboard without this link, they will see a **"Configuration Required"** error screen instead of the dashboard. The error will display: *"Please link your user account to an employee record."*

<a id="user-access-rights"></a>

## User Access Rights

In addition to linking the employee record, the user must have the correct **access rights** to read HR data. Without these permissions, the dashboard will show **"Failed to load attendance data"**.

<a id="step-1-open-user-settings"></a>

### Step 1: Open User Settings

Login as **Admin**. Go to **Settings > Users & Companies > Users** and open the user (e.g., Marc Demo).

<a id="step-2-set-human-resources-access"></a>

### Step 2: Set Human Resources Access

Under the **Human Resources** section, set the following permissions:

| Permission | Minimum Level |
| --- | --- |
| **Time Off** | Officer |
| **Attendances** | Officer |

<a id="step-3-save"></a>

### Step 3: Save

Click **Save**. The user can now access the dashboard and all attendance, leave, and holiday data will load correctly.

Important

Without **Time Off: Officer** and **Attendances: Officer** access rights, the dashboard will fail to load even if the employee-user link is correctly set up. This is because the dashboard reads data from `hr.leave`, `hr.attendance`, `resource.calendar.leaves`, and `hr.leave.allocation` models which require these permissions.

<a id="configuration"></a>

## Configuration

tip

**No additional configuration required.** The dashboard automatically adapts based on the logged-in employee, company calendar, and approved attendance & leave records.

While the module works out of the box, here are the areas that affect what the dashboard displays:

<a id="employee-linking"></a>

### Employee Linking

Each Odoo user who wants to access the dashboard must be linked to an employee record (see above). Additionally, the user must have **Time Off: Officer** and **Attendances: Officer** access rights.

<a id="leave-types"></a>

### Leave Types

The dashboard displays leave balances for all leave types that have allocations assigned to the employee:

1. Go to **Time Off > Configuration > Leave Types**
2. Set up leave types such as **Casual Leave**, **Sick Leave**, **Annual Leave**, etc. Ensure **"Requires Allocation"** is set to **Yes** for types you want to track balances for
3. Go to **Time Off > Managers > Allocation** and create allocations for each leave type per employee

<a id="public-holidays"></a>

### Public Holidays

Public holidays are displayed on the calendar as **purple-coded** days:

1. Go to **Time Off > Configuration > Public Holidays**
2. Create holiday entries with the name and date
3. The dashboard automatically picks these up and marks them on the calendar

info

The **Joining Date** field (added by this module to the Employee form) is used to calculate work anniversaries. Make sure it is filled in for employees whose anniversaries you want to display in the Celebrations panel.

<a id="configuration-summary"></a>

### Configuration Summary

| Setting | Where to Configure | Effect on Dashboard |
| --- | --- | --- |
| **Employee-User Link** | Employee Form > HR Settings > Related User | Dashboard will not load without this link |
| **Leave Types** | Time Off > Configuration > Leave Types | Determines which leave balances are shown |
| **Leave Allocations** | Time Off > Managers > Allocation | Sets the total & remaining days per leave type |
| **Public Holidays** | Time Off > Configuration > Public Holidays | Shows purple-coded holiday markers on the calendar |
| **Joining Date** | Employee Form (after Manager field) | Enables work anniversary display in Celebrations |
| **Birthday** | Employee Form > Private Information | Enables birthday display in Celebrations |
| **Project Assignments** | Project > Tasks (assign user to tasks) | Shows assigned projects in the Projects panel |

<a id="next-steps"></a>

## Next Steps

- [Dashboard Overview](../../../usage-guide/17.0/usage/dashboard-overview.md) - Learn the dashboard layout and widgets
- [Attendance Tracking](../../../usage-guide/17.0/usage/attendance-tracking.md) - Check-in/out, work timer, and statistics
- [Leave Management](../../../usage-guide/17.0/usage/leave-management.md) - Leave balances, holidays, and celebrations

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [HRMS Dashboard - Installation & Setup](https://docs.sdlccorp.com/docs/17.0/hrms-dashboard/getting-started/setup/)
