# Forecasting & Intelligence AI

Four AI features that predict the future, score your products, and keep you informed with proactive alerts.

<a id="7-demand-forecasting"></a>

## 7. Demand Forecasting

**Model:** `amazon.demand.forecast` | **Type:** Predictive Analytics

AI predicts 30/60/90-day sales volumes based on historical data.

<a id="what-it-calculates"></a>

### What It Calculates

| Output | Description |
| --- | --- |
| **30-day forecast** | Expected sales volume next 30 days |
| **60-day forecast** | Medium-term volume projection |
| **90-day forecast** | Long-term planning horizon |
| **Reorder Point** | When to reorder to avoid stockout |
| **Suggested Reorder Qty** | How much to reorder |
| **Stockout Risk** | Low / Medium / High |
| **Seasonality** | Detected patterns (holidays, weekly cycles) |

<a id="auto-purchase-orders"></a>

### Auto Purchase Orders

When enabled, the connector can **auto-create purchase orders** for restocking based on the AI forecast. Purchase orders are created as drafts for your review.

**Menu:** AI Tools > Demand Forecast

<a id="8-product-health-score"></a>

## 8. Product Health Score

**Model:** `amazon.product.health` | **Type:** Health Scoring

Computes an overall health score **(0–100)** graded **A through F** by combining 5 dimensions:

| Dimension | What's Measured |
| --- | --- |
| **Listing Quality** | Title, bullets, images, description completeness |
| **Pricing Health** | Competitive position, Buy Box win rate |
| **Inventory Health** | Stock level, velocity, stockout history |
| **Sales Velocity** | Units per day, trend (growing/declining) |
| **Review Score** | Average rating, review count, recent trend |

<a id="outputs"></a>

### Outputs

- Overall grade (A / B / C / D / F)
- Individual dimension scores
- AI-generated recommendations
- Tracked critical alerts

**Menu:** AI Tools > Product Health Scores

tip

Focus on products with grade **D or F** first. The lowest-scoring dimension usually has the highest improvement potential.

<a id="9-smart-alert-engine"></a>

## 9. Smart Alert Engine

**Model:** `amazon.smart.alert` | **Type:** Proactive Monitoring

Automatically detects issues across your Amazon business with **13 alert types** and **4 severity levels**.

See the [Smart Alerts reference](smart-alerts.md) for the complete alert type list.

**Menu:** Alerts > Active Alerts | Alerts > Alert History

<a id="10-ai-chat-assistant"></a>

## 10. AI Chat Assistant

**Model:** `amazon.ai.chat` | **Type:** Conversational AI

Floating chat widget integrated into the Odoo interface.

<a id="capabilities"></a>

### Capabilities

- Ask questions about your Amazon business in natural language
- Get context-aware responses (knows your products, orders, inventory)
- Receive smart action suggestions
- View real-time dashboard statistics
- Accessible via REST API endpoints for custom integrations

<a id="example-questions"></a>

### Example Questions

- "What's my best-selling product this week?"
- "Which products are close to stockout?"
- "Show me products with declining sales"
- "What was my total revenue last month?"
- "Which listings have the worst health score?"

**Access:** Chat widget (bottom-right corner of Odoo)

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Forecasting & Intelligence AI](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/ai-features/forecasting-ai/)
