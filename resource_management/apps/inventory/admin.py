from django.contrib import admin
from apps.inventory.models import Inventory, Category, Location

admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Location)
