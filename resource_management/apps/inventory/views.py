from django.views import generic
from django.forms.models import model_to_dict
from apps.inventory.models import Category
from apps.inventory.models import Inventory
from django.shortcuts import render_to_response
from bootstrapform.templatetags.bootstrap import render
from .forms import InventoryForm


class InventoryCat(generic.ListView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super(InventoryCat, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

class InventoryList(generic.ListView):
    model = Inventory
    
    def get_queryset(self):
        queryset = Inventory.objects.filter(category=self.request.GET['category_id'])
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super(InventoryList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['category'] = Category.objects.filter(id=self.request.GET['category_id']).first
        return context

class createInventoryView(generic.CreateView):
    model = Inventory
    form_class = InventoryForm
    
class InventoryDetail(generic.DetailView):
    model = Inventory
    
    def get_context_data(self, **kwargs):
        context = super(InventoryDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
