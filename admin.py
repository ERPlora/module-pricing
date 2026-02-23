from django.contrib import admin

from .models import PriceList, PriceRule

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'currency', 'is_active', 'start_date']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(PriceRule)
class PriceRuleAdmin(admin.ModelAdmin):
    list_display = ['price_list', 'name', 'rule_type', 'value', 'min_quantity']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

