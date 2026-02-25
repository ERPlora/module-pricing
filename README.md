# Price Lists & Rules Module

Price lists, discount rules and pricing strategies.

## Features

- Create and manage multiple price lists with unique codes
- Currency assignment per price list
- Date-based price list validity with start and end dates
- Active/inactive price list toggling
- Flexible price rules linked to price lists
- Rule types for different pricing strategies (fixed, percentage, etc.)
- Minimum quantity thresholds for volume-based pricing
- Active/inactive rule toggling for quick adjustments

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Price Lists & Rules > Settings**

## Usage

Access via: **Menu > Price Lists & Rules**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/pricing/dashboard/` | Pricing overview and summary |
| Price Lists | `/m/pricing/pricelists/` | Create and manage price lists |
| Rules | `/m/pricing/rules/` | Define and manage price rules |
| Settings | `/m/pricing/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `PriceList` | Price list with name, code, currency, active status, and optional start/end date validity |
| `PriceRule` | Pricing rule linked to a price list with name, rule type, value, minimum quantity, and active status |

## Permissions

| Permission | Description |
|------------|-------------|
| `pricing.view_pricelist` | View price lists |
| `pricing.add_pricelist` | Create new price lists |
| `pricing.change_pricelist` | Edit price lists |
| `pricing.delete_pricelist` | Delete price lists |
| `pricing.view_pricerule` | View price rules |
| `pricing.add_pricerule` | Create new price rules |
| `pricing.change_pricerule` | Edit price rules |
| `pricing.delete_pricerule` | Delete price rules |
| `pricing.manage_settings` | Access and modify module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
