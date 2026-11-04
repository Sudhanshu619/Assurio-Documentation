# Content & Listing Optimization AI

Three AI features focused on creating high-quality, SEO-optimized Amazon listings and analyzing customer feedback.

<a id="1-ai-listing-generator"></a>

## 1. AI Listing Generator

**Model:** `amazon.ai.listing` | **Type:** Content Generation

Generates SEO-optimized product content including:

- Product titles (Amazon best practices)
- 5 bullet points with keywords
- Rich product descriptions
- Backend search keywords (max 250 chars)
- A+ content suggestions

Outputs an **SEO Score (0–100)** so you know how well-optimized your listing is.

**Menu:** AI Tools > Listing Optimiser

<a id="how-to-use"></a>

### How to Use

1. Open the product in Odoo
2. Click **AI Tools > Listing Optimiser**
3. Select the target marketplace
4. Click **Generate**
5. Review the AI-generated content
6. Edit as needed and apply to the listing

<a id="2-product-type-detection"></a>

## 2. Product Type Detection

**Model:** `amazon.product` | **Type:** Classification

AI analyzes product name, brand, and description to automatically detect the correct Amazon product type definition.

**Why this matters:** Wrong product type causes the notorious **error 4000003** that blocks listing creation. This feature prevents that error by choosing the right category automatically.

**Trigger:** Automatic during product export

<a id="how-it-works"></a>

### How It Works

When you push a product to Amazon:

1. AI reads product name, brand, and description
2. Matches against Amazon's product type definitions
3. Selects the most accurate category
4. Uses correct specialized fields for that category
5. Submits the listing without error 4000003

<a id="3-review-analysis"></a>

## 3. Review Analysis

**Model:** `amazon.review.analysis` | **Type:** Sentiment Analysis

Analyzes customer reviews to extract:

- **Positive themes** - What customers love
- **Negative themes** - What they complain about
- **Sentiment score (0–1)** - Overall positivity
- **Top complaints** - Ranked by frequency
- **Improvement suggestions** - Actionable changes to your listing

**Menu:** AI Tools > Review Analysis

<a id="example-output"></a>

### Example Output

```
Sentiment: 0.72 (Positive)
Top Positive: Quality, Value for money, Fast shipping
Top Negative: Packaging damage, Size runs small
Recommendations:
  1. Update size chart with detailed measurements
  2. Improve packaging to prevent damage
  3. Add more product images showing scale
```

tip

Run Review Analysis monthly for each active product. Trends emerge over time - what was a minor complaint can become the top reason for returns if ignored.

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

---

Source: [Content & Listing Optimization AI](https://docs.sdlccorp.com/docs/19.0/amazon-odoo-connector/ai-features/content-ai/)
