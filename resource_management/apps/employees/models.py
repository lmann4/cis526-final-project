from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Position(models.Model):
    title = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User)
    position = models.ForeignKey(Position)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)


class Schedule(models.Model):
    employee_id = models.ForeignKey(Employee, related_name='schedule_set')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    employee_sub = models.ForeignKey(Employee, related_name='sub_schedule_set')
    up_for_sub = models.BooleanField(default=False)
