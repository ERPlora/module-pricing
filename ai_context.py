"""
AI context for the Pricing module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Pricing

### Models

**PriceList** — A named set of pricing rules (e.g., Wholesale, VIP, Summer Sale).
- `name`, `code` (optional identifier)
- `currency` (3-char, default 'EUR')
- `is_active`
- `start_date`, `end_date` (DateField, optional): Validity window

**PriceRule** — A specific pricing rule within a price list.
- `price_list` FK → PriceList (related_name='rules')
- `name`
- `rule_type`: 'fixed' or other types (default 'fixed') — defines how `value` is interpreted
- `value` (Decimal): The price or adjustment value
- `min_quantity` (Decimal, default 0): Minimum quantity for this rule to apply
- `is_active`

### Key Flows

1. **Create a price list**: Create PriceList with optional date range → add PriceRules targeting specific products/quantities
2. **Apply pricing**: Look up active PriceLists (is_active=True, within date range) → find matching PriceRule by rule_type and min_quantity threshold → use rule's value as the overridden price
3. **Deactivate**: Set `is_active=False` on PriceList to stop applying its rules

### Notes
- PriceRule does not have a direct FK to inventory.Product — product targeting is expected to be implemented via the rule's `name` or externally
- This is a simple pricing framework; complex per-product price overrides may need to be built on top of these models
- `rule_type='fixed'` means `value` is the absolute price; other types (e.g., 'percentage') may represent a discount off the base price
"""
