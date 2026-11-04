# AI Features Overview

The Amazon connector includes **10 AI-powered features** across 3 categories, powered by 4 leading AI providers.

| Stat | Count |
| --- | --- |
| **AI Features** | 10 |
| **AI Providers** | 4 |
| **Categories** | 3 |
| **Alert Types** | 13 |

<a id="supported-ai-providers"></a>

## Supported AI Providers

| Provider | Model | Tier | Best For |
| --- | --- | --- | --- |
| **Groq** | LLaMA 3.3 70B Versatile | Default (Free tier) | Testing & development |
| **OpenAI** | GPT-4 / GPT-4o | Premium | Best overall accuracy |
| **Anthropic Claude** | Claude Sonnet 4 | Premium | Best reasoning & analysis |
| **Google Gemini** | Gemini 2.0 Flash | Value | Fast & affordable production |

<a id="3-ai-categories"></a>

## 3 AI Categories

<a id="category-1-content--listing-optimization-3-features"></a>

### Category 1: Content & Listing Optimization (3 features)

- AI Listing Generator
- Product Type Detection
- Review Analysis

[See Content AI features →](content-ai.md)

<a id="category-2-pricing--profitability-3-features"></a>

### Category 2: Pricing & Profitability (3 features)

- AI Price Optimizer
- Profit Calculator
- Competitor Monitor

[See Pricing AI features →](pricing-ai.md)

<a id="category-3-forecasting--intelligence-4-features"></a>

### Category 3: Forecasting & Intelligence (4 features)

- Demand Forecasting
- Product Health Score
- Smart Alert Engine
- AI Chat Assistant

[See Forecasting AI features →](forecasting-ai.md)

<a id="complete-ai-feature-index"></a>

## Complete AI Feature Index

| # | Feature | Type | Category | Odoo Model |
| --- | --- | --- | --- | --- |
| 1 | **AI Listing Generator** | Content Generation | Content & Listing | `amazon.ai.listing` |
| 2 | **Product Type Detection** | Classification | Content & Listing | `amazon.product` |
| 3 | **Review Analysis** | Sentiment Analysis | Content & Listing | `amazon.review.analysis` |
| 4 | **AI Price Optimizer** | Price Optimization | Pricing & Profit | `amazon.ai.pricing` |
| 5 | **Profit Calculator** | Financial Analysis | Pricing & Profit | `amazon.profit.calculator` |
| 6 | **Competitor Monitor** | Market Intelligence | Pricing & Profit | `amazon.competitor.monitor` |
| 7 | **Demand Forecasting** | Predictive Analytics | Forecasting & Intel | `amazon.demand.forecast` |
| 8 | **Product Health Score** | Health Scoring | Forecasting & Intel | `amazon.product.health` |
| 9 | **Smart Alert Engine** | Proactive Monitoring | Forecasting & Intel | `amazon.smart.alert` |
| 10 | **AI Chat Assistant** | Conversational AI | Forecasting & Intel | `amazon.ai.chat` |

<a id="how-to-enable-ai-features"></a>

## How to Enable AI Features

<a id="step-1---enable-ai-globally"></a>

### Step 1 - Enable AI Globally

Go to **Amazon > Configuration > Settings** and enable the **"Enable AI Features"** toggle.

<a id="step-2---configure-provider"></a>

### Step 2 - Configure Provider

Open your Amazon Instance (**Amazon > Configuration > Instances**) and in the **AI Configuration** tab:

1. Select your AI Provider (Groq, OpenAI, Claude, or Gemini)
2. Enter your **API Key** for the selected provider
3. Click **Test AI Connection** to verify the key works

<a id="step-3---enable-automation-optional"></a>

### Step 3 - Enable Automation (Optional)

Toggle the AI automation features you want:

- **Auto Pricing** - Automatic price optimization
- **Auto Listing** - AI listing generation on product creation
- **Auto Forecast** - Automatic demand forecasting
- **Review Analysis** - Auto-analyze reviews when they arrive

<a id="step-4---configure-alerts"></a>

### Step 4 - Configure Alerts

Set the **Low Stock Alert Threshold** and enable the **Smart Alert Scan** scheduled action for proactive monitoring.

Provider Selection

Start with **Groq** (free tier) for testing. Switch to **OpenAI GPT-4** or **Claude** for production-quality AI outputs. **Google Gemini** is a great middle ground for cost-effective production use.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [AI Features Overview](https://docs.sdlccorp.com/docs/amazon-odoo-connector/ai-features/overview/)
