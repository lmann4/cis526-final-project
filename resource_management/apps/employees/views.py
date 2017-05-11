import json
from datetime import date, timedelta

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

from apps.base.views import NavbarMixin
from apps.employees.forms import ScheduleForm
from apps.employees.models import Employee, Schedule


class EmployeeDetail(NavbarMixin, generic.DetailView):
    model = Employee

    def get_week_schedule_data(self):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        schedule = Schedule.objects.filter(employee__user_id=self.request.user.pk, date__gte=week_start, date__lte=week_end).order_by('date')

        work_week = {}
        for shift in schedule:
            work_week[shift.date.weekday()] = {
                'start_time': shift.start_time.strftime('%I:%H %p'),
                'end_time': shift.end_time.strftime('%I:%H %p'),
                'is_sub_shift': shift.employee_sub == self.request.user.pk
            }
        return json.dumps(work_week)


def home(request):
    return HttpResponseRedirect(reverse('employees:employee_detail', args=[Employee.objects.filter(user_id=request.user).first().pk]))


def schedule(request):
    return HttpResponseRedirect(reverse('employees:employee_admin'))


class ScheduleAdd(NavbarMixin, generic.FormView):
    template_name = "employees/schedule_form.html"
    form_class = ScheduleForm
    success_url = reverse_lazy('employees:employee_admin')


class EmployeeAdminPanel(NavbarMixin, generic.TemplateView):
    template_name = "employees/employee_admin.html"
