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
