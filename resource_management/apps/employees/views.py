from django.views import generic

from apps.employees.models import Employee


class EmployeeDetail(generic.DetailView):
    model = Employee
