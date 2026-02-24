from django import forms
from django.utils.translation import gettext_lazy as _

from .models import PriceList

class PriceListForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = ['name', 'code', 'currency', 'is_active', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'code': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'currency': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle'}),
            'start_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
        }

