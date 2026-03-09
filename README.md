# Price Lists & Rules

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `pricing` |
| **Version** | `1.0.0` |
| **Icon** | `pricetag-outline` |
| **Dependencies** | None |

## Models

### `PriceList`

PriceList(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, name, code, currency, is_active, start_date, end_date)

| Field | Type | Details |
|-------|------|---------|
| `name` | CharField | max_length=255 |
| `code` | CharField | max_length=50, optional |
| `currency` | CharField | max_length=3 |
| `is_active` | BooleanField |  |
| `start_date` | DateField | optional |
| `end_date` | DateField | optional |

### `PriceRule`

PriceRule(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, price_list, name, rule_type, value, min_quantity, is_active)

| Field | Type | Details |
|-------|------|---------|
| `price_list` | ForeignKey | → `pricing.PriceList`, on_delete=CASCADE |
| `name` | CharField | max_length=255 |
| `rule_type` | CharField | max_length=20 |
| `value` | DecimalField |  |
| `min_quantity` | DecimalField |  |
| `is_active` | BooleanField |  |

## Cross-Module Relationships

| From | Field | To | on_delete | Nullable |
|------|-------|----|-----------|----------|
| `PriceRule` | `price_list` | `pricing.PriceList` | CASCADE | No |

## URL Endpoints

Base path: `/m/pricing/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `pricelists/` | `pricelists` | GET |
| `rules/` | `rules` | GET |
| `price_lists/` | `price_lists_list` | GET |
| `price_lists/add/` | `price_list_add` | GET/POST |
| `price_lists/<uuid:pk>/edit/` | `price_list_edit` | GET |
| `price_lists/<uuid:pk>/delete/` | `price_list_delete` | GET/POST |
| `price_lists/<uuid:pk>/toggle/` | `price_list_toggle_status` | GET |
| `price_lists/bulk/` | `price_lists_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `pricing.view_pricelist` | View Pricelist |
| `pricing.add_pricelist` | Add Pricelist |
| `pricing.change_pricelist` | Change Pricelist |
| `pricing.delete_pricelist` | Delete Pricelist |
| `pricing.view_pricerule` | View Pricerule |
| `pricing.add_pricerule` | Add Pricerule |
| `pricing.change_pricerule` | Change Pricerule |
| `pricing.delete_pricerule` | Delete Pricerule |
| `pricing.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_pricelist`, `add_pricerule`, `change_pricelist`, `change_pricerule`, `view_pricelist`, `view_pricerule`
- **employee**: `add_pricelist`, `view_pricelist`, `view_pricerule`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Price Lists | `pricetag-outline` | `pricelists` | No |
| Rules | `options-outline` | `rules` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_price_lists`

List price lists with their status.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `active_only` | boolean | No | Only show active price lists |

### `get_price_list`

Get a price list with all its pricing rules.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `price_list_id` | string | Yes | Price list ID |

### `create_price_list`

Create a new price list.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Price list name |
| `code` | string | No | Short code |
| `currency` | string | No | Currency code (e.g. EUR, USD) |
| `start_date` | string | No | Start date (YYYY-MM-DD) |
| `end_date` | string | No | End date (YYYY-MM-DD) |

### `add_price_rule`

Add a pricing rule to a price list.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `price_list_id` | string | Yes | Price list ID |
| `name` | string | Yes | Rule name |
| `rule_type` | string | No | fixed, percentage, markup (default: fixed) |
| `value` | string | Yes | Rule value (price or percentage) |
| `min_quantity` | integer | No | Minimum quantity to apply rule |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  icons/
    icon.svg
  pricing/
    css/
    js/
templates/
  pricing/
    pages/
      dashboard.html
      index.html
      price_list_add.html
      price_list_edit.html
      price_lists.html
      pricelists.html
      rules.html
      settings.html
    partials/
      dashboard_content.html
      panel_price_list_add.html
      panel_price_list_edit.html
      price_list_add_content.html
      price_list_edit_content.html
      price_lists_content.html
      price_lists_list.html
      pricelists_content.html
      rules_content.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
