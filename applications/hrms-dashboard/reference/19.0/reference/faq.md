# HRMS Dashboard - FAQ & Troubleshooting

Common questions and solutions for the HRMS Employee Dashboard module.

<a id="frequently-asked-questions"></a>

## Frequently Asked Questions

<a id="the-dashboard-shows-configuration-required-error-what-should-i-do"></a>

### The dashboard shows "Configuration Required" error. What should I do?

This means your Odoo **user account is not linked to an employee record**. An Administrator must fix this:

1. Login as **Admin**
2. Go to **Employees > Employees**
3. Open your employee record
4. Go to the **HR Settings** tab and set the **Related User** field to your Odoo user account
5. Save and refresh the dashboard page

<a id="the-dashboard-shows-failed-to-load-attendance-data-what-should-i-do"></a>

### The dashboard shows "Failed to load attendance data". What should I do?

This means your user account does not have sufficient **access rights** to read HR data, even though the employee-user link is correct. An Administrator must fix this:

1. Login as **Admin**
2. Go to **Settings > Users & Companies > Users**
3. Open the user account
4. Under **Human Resources**, set **Time Off** to at least **Officer**
5. Set **Attendances** to at least **Officer**
6. Save and ask the user to refresh the dashboard

<a id="why-is-the-calendar-showing-absent-for-days-i-was-present"></a>

### Why is the calendar showing "Absent" for days I was present?

The dashboard relies on **attendance records** (check-in/check-out) in Odoo. If you were present but did not check in via the attendance module, the day will appear as absent. Ensure that attendance is being recorded either through:

- This dashboard's **Check In / Check Out** buttons
- The Odoo **Attendance** module
- An integrated **biometric device**

<a id="why-dont-i-see-any-celebrations-or-projects-on-the-dashboard"></a>

### Why don't I see any celebrations or projects on the dashboard?

**Celebrations:** Birthdays require the `birthday` field on employee records. Work anniversaries require the `joining_date` field (added by this module). Only events within the next 30 days are shown.

**Projects:** You must be assigned to tasks within a project. Go to **Project > Tasks** and ensure you are listed as an assignee on at least one task.

<a id="does-the-timer-keep-running-if-i-close-the-browser"></a>

### Does the timer keep running if I close the browser?

The live timer is a **frontend display only**. Your check-in record is stored on the server with the timestamp. When you re-open the dashboard, the timer recalculates the elapsed time from your stored check-in record, so **no time is lost**.

<a id="what-timezone-does-the-dashboard-use"></a>

### What timezone does the dashboard use?

All times are converted from UTC to the **user's configured timezone**. You can set your timezone in **Preferences**:

1. Click your avatar in the top-right corner
2. Go to **My Profile > Preferences > Timezone**
3. Select your timezone and save

<a id="security--access-control"></a>

## Security & Access Control

The module uses the following access control rules:

| Model | Group | Read | Write | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| `attendance.dashboard` | Internal User | Yes | Yes | Yes | Yes |
| `attendance.dashboard.setup` | Internal User | Yes | Yes | Yes | Yes |

All authenticated internal users have full access to the dashboard model. However, users also need **Time Off: Officer** and **Attendances: Officer** access rights to read the underlying HR data. The dashboard is designed so that **each employee can only view their own attendance data**.

<a id="supported-versions"></a>

## Supported Versions

| Property | Value |
| --- | --- |
| **Odoo Version** | 17.0, 18.0, 19.0 |
| **Edition** | Community |
| **Module Version** | 17, 18, 19 |
| **License** | LGPL-3 |
| **Category** | Human Resources |
| **Author** | SDLC Corp |

<a id="dependencies"></a>

## Dependencies

| Module | Technical Name | Purpose |
| --- | --- | --- |
| **Base** | `base` | Core Odoo framework (users, groups, access rights) |
| **Employees** | `hr` | Employee records, departments, and the employee form |
| **Attendances** | `hr_attendance` | Attendance records (check-in/check-out data) |
| **Time Off** | `hr_holidays` | Leave types, leave requests, allocations, and public holidays |
| **Project** | `project` | Project and task data for the Projects panel |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [HRMS Dashboard - FAQ & Troubleshooting](https://docs.sdlccorp.com/docs/19.0/hrms-dashboard/reference/faq/)
