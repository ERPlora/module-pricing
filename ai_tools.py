"""AI tools for the Pricing module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListPriceLists(AssistantTool):
    name = "list_price_lists"
    description = "List price lists with their status."
    module_id = "pricing"
    required_permission = "pricing.view_pricelist"
    parameters = {
        "type": "object",
        "properties": {
            "active_only": {"type": "boolean", "description": "Only show active price lists"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from pricing.models import PriceList
        qs = PriceList.objects.all().order_by('name')
        if args.get('active_only'):
            qs = qs.filter(is_active=True)
        return {
            "price_lists": [
                {
                    "id": str(pl.id),
                    "name": pl.name,
                    "code": pl.code,
                    "currency": pl.currency,
                    "is_active": pl.is_active,
                    "start_date": str(pl.start_date) if pl.start_date else None,
                    "end_date": str(pl.end_date) if pl.end_date else None,
                    "rules_count": pl.rules.count(),
                }
                for pl in qs
            ]
        }


@register_tool
class GetPriceList(AssistantTool):
    name = "get_price_list"
    description = "Get a price list with all its pricing rules."
    module_id = "pricing"
    required_permission = "pricing.view_pricelist"
    parameters = {
        "type": "object",
        "properties": {"price_list_id": {"type": "string", "description": "Price list ID"}},
        "required": ["price_list_id"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from pricing.models import PriceList
        pl = PriceList.objects.get(id=args['price_list_id'])
        rules = pl.rules.filter(is_active=True).order_by('name')
        return {
            "id": str(pl.id), "name": pl.name, "code": pl.code,
            "currency": pl.currency, "is_active": pl.is_active,
            "start_date": str(pl.start_date) if pl.start_date else None,
            "end_date": str(pl.end_date) if pl.end_date else None,
            "rules": [
                {"id": str(r.id), "name": r.name, "rule_type": r.rule_type,
                 "value": str(r.value), "min_quantity": r.min_quantity}
                for r in rules
            ],
        }


@register_tool
class CreatePriceList(AssistantTool):
    name = "create_price_list"
    description = "Create a new price list."
    module_id = "pricing"
    required_permission = "pricing.add_pricelist"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Price list name"},
            "code": {"type": "string", "description": "Short code"},
            "currency": {"type": "string", "description": "Currency code (e.g. EUR, USD)"},
            "start_date": {"type": "string", "description": "Start date (YYYY-MM-DD)"},
            "end_date": {"type": "string", "description": "End date (YYYY-MM-DD)"},
        },
        "required": ["name"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from pricing.models import PriceList
        pl = PriceList.objects.create(
            name=args['name'],
            code=args.get('code', ''),
            currency=args.get('currency', 'EUR'),
            start_date=args.get('start_date'),
            end_date=args.get('end_date'),
            is_active=True,
        )
        return {"id": str(pl.id), "name": pl.name, "created": True}


@register_tool
class AddPriceRule(AssistantTool):
    name = "add_price_rule"
    description = "Add a pricing rule to a price list."
    module_id = "pricing"
    required_permission = "pricing.add_pricerule"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "price_list_id": {"type": "string", "description": "Price list ID"},
            "name": {"type": "string", "description": "Rule name"},
            "rule_type": {"type": "string", "description": "fixed, percentage, markup (default: fixed)"},
            "value": {"type": "string", "description": "Rule value (price or percentage)"},
            "min_quantity": {"type": "integer", "description": "Minimum quantity to apply rule"},
        },
        "required": ["price_list_id", "name", "value"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from decimal import Decimal
        from pricing.models import PriceRule
        r = PriceRule.objects.create(
            price_list_id=args['price_list_id'],
            name=args['name'],
            rule_type=args.get('rule_type', 'fixed'),
            value=Decimal(args['value']),
            min_quantity=args.get('min_quantity', 1),
            is_active=True,
        )
        return {"id": str(r.id), "name": r.name, "created": True}
