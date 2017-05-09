from django import forms
from apps.inventory.models import Inventory

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['name', 'category', 'location', 'amount', 'units']