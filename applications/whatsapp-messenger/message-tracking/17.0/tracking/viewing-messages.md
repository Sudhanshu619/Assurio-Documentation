# Viewing & Tracking Messages


<a id="overview"></a>

## Overview

Every WhatsApp message sent through the connector is logged so you can confirm delivery, retry failures, and audit what was sent to whom. This page covers the two places that log surfaces in Odoo: the dedicated message log and the document chatter.

<a id="message-log"></a>

## Message Log

Go to **WhatsApp Messenger > Messages** to see all sent messages:

![Messages Log](https://docs.sdlccorp.com/assets/images/messages-blog-1786e320fd1640b0a27164342c3f759d.webp)

| Column | Description |
| --- | --- |
| **Date** | When the message was sent |
| **Recipient** | Customer name |
| **Phone Number** | Recipient's WhatsApp number |
| **Message** | Message content preview |
| **Document** | Linked sale order or invoice |
| **Status** | Current delivery status |

<a id="message-statuses"></a>

## Message Statuses

| Status | Meaning |
| --- | --- |
| **Draft** | Message created but not yet sent |
| **Sent** | Message sent to WhatsApp servers |
| **Delivered** | Message delivered to recipient's device |
| **Read** | Recipient has read the message |
| **Failed** | Delivery failed: check failure reason |

<a id="viewing-from-document-chatter"></a>

## Viewing from Document Chatter

Every WhatsApp message is also logged in the document's chatter (activity feed). Open any Sale Order or Invoice to see entries like:

> "WhatsApp message sent to +91XXXXXXXXXX with PDF attached"

<a id="retrying-failed-messages"></a>

## Retrying Failed Messages

1. Go to **WhatsApp Messenger > Messages**
2. Find the message with **Failed** status
3. Open it to see the **Failure Reason**
4. Click **Retry**
5. On success, status changes to **Sent**

<a id="changing-phone-numbers"></a>

## Changing Phone Numbers

**From the composer:** Edit the WhatsApp Number field and check **"Save phone to contact"** to persist it.

**From Contacts:** Go to **Contacts**, open the contact, edit the **Mobile** or **Phone** field.

tip

Always include the country code (e.g., +91 for India, +1 for US). The module automatically strips special characters.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Viewing & Tracking Messages](https://docs.sdlccorp.com/docs/17.0/whatsapp-messenger/tracking/viewing-messages/)
