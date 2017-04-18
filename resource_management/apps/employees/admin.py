from django.contrib import admin
from apps.employees.models import Employee, Position

admin.site.register(Employee)
admin.site.register(Position)
