from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from apps.employees.models import Employee


class EmployeeDetail(generic.DetailView):
    model = Employee


def home(request):
    return HttpResponseRedirect(reverse('employees:employee_detail', args=[Employee.objects.filter(user_id=request.user).first().pk]))
