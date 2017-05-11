from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^home/$', login_required(views.home), name="employee_home_redirect"),
    url(r'^(?P<pk>[\d]+)/$', login_required(views.EmployeeDetail.as_view()), name="employee_detail"),
    url(r'^schedule/add$', login_required(views.ScheduleAdd.as_view()), name="employee_schedule_add"),
    url(r'^schedule/$', login_required(views.schedule), name="employee_schedule"),
    url(r'^admin/$', login_required(views.EmployeeAdminPanel.as_view()), name="employee_admin"),
)
