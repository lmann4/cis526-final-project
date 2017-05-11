import json
from datetime import date, timedelta

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from apps.base.views import NavbarMixin
from apps.employees.forms import ScheduleForm
from apps.employees.models import Employee, Schedule


class EmployeeDetail(NavbarMixin, generic.DetailView):
    model = Employee

    def get_week_schedule_data(self):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        schedule = Schedule.objects.filter(Q(employee__user_id=self.request.user.pk) | Q(employee_sub__user_id=self.request.user.pk), date__gte=week_start, date__lte=week_end).order_by('date')

        work_week = {}
        for shift in schedule:
            is_sub_shift = False
            shift_taken = False
            if shift.employee_sub and shift.employee_sub.user.id == self.request.user.pk and shift.up_for_sub is False:
                is_sub_shift = True
            if shift.employee_sub and shift.employee_sub.user.id != self.request.user.pk and shift.up_for_sub is False:
                shift_taken = True
            work_week[shift.date.weekday()] = {
                'start_time': shift.start_time.strftime('%I:%H %p'),
                'end_time': shift.end_time.strftime('%I:%H %p'),
                'is_sub_shift': is_sub_shift,
                'up_for_sub': shift.up_for_sub,
                'shift_taken': shift_taken
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


class SubBoard(NavbarMixin, generic.TemplateView):
    template_name = "employees/sub_board.html"

    def sub_slips(self):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=12)

        return Schedule.objects.filter(up_for_sub=1, employee_sub=None, date__gte=week_start, date__lte=week_end).order_by('date')
