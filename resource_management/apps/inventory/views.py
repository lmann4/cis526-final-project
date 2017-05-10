from django.views import generic

from apps.base.views import NavbarMixin
from apps.inventory.models import Category
from apps.inventory.models import Inventory
from .forms import InventoryForm


class InventoryCat(generic.ListView, NavbarMixin):
    model = Category


class InventoryList(generic.ListView, NavbarMixin):
    model = Inventory
    
    def get_queryset(self):
        queryset = Inventory.objects.filter(category=self.request.GET['category_id'])
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super(InventoryList, self).get_context_data()
        context['category'] = Category.objects.filter(id=self.request.GET['category_id']).first
        return context


class createInventoryView(generic.CreateView, NavbarMixin):
    model = Inventory
    form_class = InventoryForm


class InventoryDetail(generic.DetailView, NavbarMixin):
    model = Inventory
