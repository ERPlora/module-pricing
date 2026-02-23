from django.utils.translation import gettext_lazy as _

MODULE_ID = 'pricing'
MODULE_NAME = _('Price Lists & Rules')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'pricetag-outline'
MODULE_DESCRIPTION = _('Price lists, discount rules and pricing strategies')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'commerce'

MENU = {
    'label': _('Price Lists & Rules'),
    'icon': 'pricetag-outline',
    'order': 18,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Price Lists'), 'icon': 'pricetag-outline', 'id': 'pricelists'},
{'label': _('Rules'), 'icon': 'options-outline', 'id': 'rules'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'pricing.view_pricelist',
'pricing.add_pricelist',
'pricing.change_pricelist',
'pricing.delete_pricelist',
'pricing.view_pricerule',
'pricing.add_pricerule',
'pricing.change_pricerule',
'pricing.delete_pricerule',
'pricing.manage_settings',
]
