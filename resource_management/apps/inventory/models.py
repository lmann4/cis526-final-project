from django.db import models
from django.urls import reverse

INVENTORY_UNITS = (
    (0, 'Count'),
    (1, 'Pounds'),
    (2, 'Ounces'),
    (3, 'Liters')
)


# what type of item it is (i.e. Produce, Freezer, etc.)
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Where the item is stored (i.e. Freezer A)
class Location(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    units = models.SmallIntegerField(choices=INVENTORY_UNITS, default=0)
    
    def get_absolute_url(self):
        return reverse('inventory_detail', kwargs={'pk': self.pk})
