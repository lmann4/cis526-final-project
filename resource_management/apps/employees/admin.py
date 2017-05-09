from django.contrib import admin
from apps.employees.models import Employee, Position, Schedule

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Schedule)
