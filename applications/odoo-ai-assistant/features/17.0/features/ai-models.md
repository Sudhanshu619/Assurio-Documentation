# AI Models & Data Areas


<a id="overview"></a>

## Overview

The Odoo AI Assistant works with several AI providers so you can pick the right tradeoff between price, latency, and accuracy. This page lists the supported models, how the auto-fallback chain works, and which Odoo data areas every model can query.

<a id="available-ai-models"></a>

## Available AI Models

Switch between 6 models from the dropdown at the top of the chat:

![AI Model Selection](https://docs.sdlccorp.com/assets/images/ai-models-1585d069445be2a4d79f671376fa6d94.webp)

| Model | Strength | Best For |
| --- | --- | --- |
| **Llama 3.3 70B (Smart)** | High accuracy | General business queries (recommended) |
| **Llama 3.1 8B (Fast)** | Speed | Simple lookups, quick answers |
| **DeepSeek R1 (Deep)** | Deep reasoning | Complex analytics, multi-step queries |
| **Kimi K2 (Powerful)** | Advanced AI | Nuanced business questions |
| **GPT O3 128k (Largest)** | Large context | Queries involving lots of data |
| **GPT O3 20B** | Balanced | Good all-round performance |

<a id="auto-fallback"></a>

### Auto-Fallback

If your selected model hits a rate limit, the AI automatically switches to the next available model. no interruption, no error message.

<a id="18-queryable-data-areas"></a>

## 18 Queryable Data Areas

| Area | What You Can Ask |
| --- | --- |
| **Contacts** | Names, emails, phones, addresses, countries |
| **CRM Leads** | Lead stages, expected revenue, probability |
| **Sales Orders** | Order totals, status, dates, customers |
| **Order Lines** | Products, quantities, unit prices |
| **Employees** | Names, departments, managers, positions |
| **Departments** | Department names, member counts |
| **Job Positions** | Open positions, descriptions |
| **Products** | Names, prices, categories, types |
| **Categories** | Product category hierarchy |
| **Invoices** | Amounts, due dates, payment status |
| **Payments** | Payment amounts, methods, dates |
| **Sales Teams** | Team names, members, targets |
| **CRM Stages** | Pipeline stages, win rates |
| **Transfers** | Stock transfers, picking status |
| **Warehouses** | Warehouse names, locations |
| **Stock** | Current stock levels, quantities |
| **Calendar** | Events, meetings, schedules |
| **Companies** | Company names, multi-company data |

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [AI Models & Data Areas](https://docs.sdlccorp.com/docs/17.0/odoo-ai-assistant/features/ai-models/)
