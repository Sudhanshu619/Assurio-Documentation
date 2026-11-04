# Admin Configuration

Administrators can configure the AI provider, default model, and user access.

<a id="api-key-setup"></a>

## API Key Setup

Go to the AI Assistant configuration page:

![Configuration](https://docs.sdlccorp.com/assets/images/configuration-model-4f954c5951e2c27697fa1cd9b2e21090.webp)

| Setting | Description |
| --- | --- |
| **Groq API Key** | Your Groq Cloud API key (free tier available at [console.groq.com](https://console.groq.com)) |
| **Model in Use** | Default AI model for all users |
| **Temperature** | Creativity level (0.1 = precise, 1.0 = creative). Default: 0.10 |
| **Max Tokens** | Maximum response length. Default: 1,024 |
| **Timeout** | Request timeout in seconds. Default: 60 |

<a id="access-control"></a>

## Access Control

Set user permissions in **Settings > Users > Access Rights**:

![Access Control](https://docs.sdlccorp.com/assets/images/access-control-66ed1f7b38a552c6147884e71898bc67.webp)

<a id="three-access-roles"></a>

### Three Access Roles

| Role | Permissions |
| --- | --- |
| **No Access** | AI Assistant is completely hidden |
| **User: Chat Only** | Can chat with AI and view own conversation history |
| **Admin: Full Access** | Chat + configure AI settings, models, and user access |

<a id="setting-permissions"></a>

### Setting Permissions

1. Go to **Settings > Users & Companies > Users**
2. Open the user record
3. Click the **Access Rights** tab
4. Find **AI Assistant** under the "Other" section
5. Select the appropriate role from the dropdown
6. Click **Save**

<a id="intent-mappings"></a>

## Intent Mappings

Admins can enable or disable specific data areas that the AI can query. Go to the AI Assistant configuration to manage which of the 18 business areas are available to users.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Admin Configuration](https://docs.sdlccorp.com/docs/odoo-ai-assistant/configuration/admin-setup/)
