# Import Locations


<a id="why-locations-matter"></a>

## Why locations matter

If your Shopify store ships from more than one location (warehouse, third-party fulfilment service, store back-room), Shopify orders carry a Location ID that tells the connector where each order should ship from. Mapping each Shopify location to an Odoo warehouse is what makes that routing land in the right Odoo warehouse instead of falling back to a single default.

<a id="overview"></a>

## Overview

Shopify orders carry a Location ID that tells the connector which inventory pool the order is supposed to ship from. Importing Shopify locations and mapping each one to an Odoo warehouse is what makes that routing work - otherwise every order falls back to the connector's default warehouse.

Import your Shopify fulfilment locations into Odoo for warehouse mapping.

<a id="importing-locations"></a>

## Importing Locations

1. Navigate to **Shopify → Operations → Import Locations**
2. Select your **Shopify Instance**
3. Click **Import Locations**

<a id="mapping-locations-to-warehouses"></a>

## Mapping Locations to Warehouses

After import:

1. Go to **Shopify → Configuration → Location Mapping**
2. For each Shopify location, select the matching **Odoo Internal Location**
3. Save

Need Help?

Contact SDLC Corp at [sdlccorp.com/contact-us](https://sdlccorp.com/contact-us/) or email **[sales@sdlccorp.com](mailto:sales@sdlccorp.com)**

<a id="related"></a>

## Related

- [Import Stock](../../../products/17.0/products/import-stock.md) - once locations map to warehouses, stock import lands in the right warehouse.
- [Configure Instance](../../../installation/17.0/installation/configure-instance.md) - set the default warehouse used when no location matches.
- [Stock Information](../../../configuration/17.0/configuration/stock-information.md) - choose the stock-update direction and behaviour.

---

Source: [Import Locations](https://docs.sdlccorp.com/docs/17.0/shopify-odoo-connector/operations/import-location/)
