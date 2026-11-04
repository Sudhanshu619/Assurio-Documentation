# Signing in

The four public screens - sign in, register, forgot password, reset password - and how sessions actually work.

<a id="intro"></a>

## Before you are signed in

These are the only screens a signed-out visitor can reach. They share a split layout: the form on the left where it is reachable, the product story on the right - which collapses away entirely below a large screen, so a phone gets the form full-bleed.

Everything else in the console redirects to `/login`, remembering where you were headed so you land there after signing in.

<a id="login"></a>

## Sign in

**Route:** `/login`

Email and password. On success the server sets a session cookie and the console bootstraps your identity, permissions and navigation.

**What you see**

- Email and password fields with an inline show/hide toggle
- A link to the forgot-password flow and to registration

**What you can do**

- Sign in
- Start a password reset

**Good to know:** Already signed in? This route bounces you to the dashboard rather than showing a second login form.

<a id="register"></a>

## Create account

**Route:** `/register`

Public self-registration. A new account joins the default organization as an API Consumer - the portal-side role - not as an operator.

**What you see**

- First name, last name, email, password and confirmation
- A live password-strength checklist: length, upper, lower, digit, symbol
- Whether self-registration is currently open

**What you can do**

- Create an account and be signed in immediately

**Good to know:** Registration can be closed entirely, which is the usual setting for an internal deployment where accounts are invited from [Administration → Users](admin.md#users).

<a id="forgot"></a>

## Forgot password

**Route:** `/forgot-password`

Requests a time-limited reset link by email.

**What you see**

- A single email field, and a confirmation panel once submitted
- In development - where no SMTP host is configured - the reset link itself, so the flow stays testable

**What you can do**

- Request a reset link
- Return to sign in

**Good to know:** The response is deliberately identical whether or not the address exists. Confirming which emails have accounts is an information leak, so the screen never does.

<a id="reset"></a>

## Set a new password

**Route:** `/reset-password/:token`

Consumes the token from the reset email and sets a new password.

**What you see**

- New password and confirmation with the same strength checklist
- A clear failure state if the token has expired or was already used

**What you can do**

- Set the new password, then sign in with it

**Good to know:** Completing a reset **revokes every existing session** for that user, on every device. That is the point: if the reset was triggered because an account was compromised, the attacker is signed out at the same moment.

<a id="sessions"></a>

## How the session works

Worth understanding, because it explains several behaviours elsewhere in the console.

- Signing in sets an **HttpOnly cookie** (`cx_sid`) backed by a row in a sessions table. JavaScript cannot read it, so a cross-site scripting bug cannot steal your credential.
- The browser never holds a token. There is no refresh interceptor and nothing in local storage to leak.
- Because the session is a database row, deleting it revokes access **immediately** - which is what makes “sign out everywhere”, a password reset and a role change all take effect at once.
- Expiry slides: 30 days by default, refreshed on use.

| If this happens | You will see |
| --- | --- |
| Your session expires or is revoked | The next request returns 401 and the console returns you to sign in |
| An administrator changes your role | You are signed out; signing back in gives you the new navigation |
| You reset your password | Every device is signed out, including the one you did it from |
| You change your password from your profile | Other devices are signed out; the one you used stays |

<a id="errors"></a>

## Access denied and Not found

<a id="access-denied"></a>

### Access denied

**Route:** `/access-denied`

Where the route guard sends you when you open a page your role does not hold the permission for.

**What you see**

- Which page was refused
- A route back to the dashboard

**What you can do**

- Return to the dashboard

**Good to know:** This is a convenience, not the security boundary. The API would refuse the underlying calls even if the page rendered.

<a id="not-found"></a>

### Not found

**Route:** `* (any unmatched route)`

A mistyped URL inside the console.

**What you see**

- A 404 panel and a link home

**What you can do**

- Return to the dashboard

Two different refusals

`/access-denied` means the page exists but your role may not open it. A not-found means no such page. If you land on the first, the fix is a permission - see [Roles & permissions](../../../getting-started/current/getting-started/roles.md).

---

Source: [Signing in](https://docs.sdlccorp.com/docs/conflux/console/auth/)
