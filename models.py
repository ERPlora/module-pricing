from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

class PriceList(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    code = models.CharField(max_length=50, blank=True, verbose_name=_('Code'))
    currency = models.CharField(max_length=3, default='EUR', verbose_name=_('Currency'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    start_date = models.DateField(null=True, blank=True, verbose_name=_('Start Date'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('End Date'))

    class Meta(HubBaseModel.Meta):
        db_table = 'pricing_pricelist'

    def __str__(self):
        return self.name


class PriceRule(HubBaseModel):
    price_list = models.ForeignKey('PriceList', on_delete=models.CASCADE, related_name='rules')
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    rule_type = models.CharField(max_length=20, default='fixed', verbose_name=_('Rule Type'))
    value = models.DecimalField(max_digits=12, decimal_places=2, default='0', verbose_name=_('Value'))
    min_quantity = models.DecimalField(max_digits=10, decimal_places=2, default='0', verbose_name=_('Min Quantity'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    class Meta(HubBaseModel.Meta):
        db_table = 'pricing_pricerule'

    def __str__(self):
        return self.name

