from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from apps.base.views import NavbarMixin
from apps.employees.forms import ScheduleForm
from apps.employees.models import Employee, Schedule
from apps.inventory.models import Category


class EmployeeDetail(NavbarMixin, generic.DetailView):
    model = Employee

    def get_week_schedule_data(self):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        schedule = Schedule.objects.filter(employee_id=self.request.user.pk, date__gte=week_start, date__lte=week_end).order_by('date')

        work_week = {}
        for shift in schedule:
            work_week[shift.date.weekday()] = {
                'start_time': shift.start_time.strftime('%I:%H %p'),
                'end_time': shift.end_time.strftime('%I:%H %p'),
                'is_sub_shift': shift.employee_sub == self.request.user.pk
            }
        return work_week

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


def home(request):
    return HttpResponseRedirect(reverse('employees:employee_detail', args=[Employee.objects.filter(user_id=request.user).first().pk]))


class ScheduleAdd(NavbarMixin, generic.CreateView):
    model = Schedule
    form_class = ScheduleForm
