from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.employees import ajax
from . import views

urlpatterns = (
    url(r'^home/$', login_required(views.home), name="employee_home_redirect"),
    url(r'^(?P<pk>[\d]+)/$', login_required(views.EmployeeDetail.as_view()), name="employee_detail"),
    url(r'^schedule/add$', login_required(views.ScheduleAdd.as_view()), name="employee_schedule_add"),
    url(r'^schedule/$', login_required(views.schedule), name="employee_schedule"),
    url(r'^admin/$', login_required(views.EmployeeAdminPanel.as_view()), name="employee_admin"),
    url(r'^sub-board/$', login_required(views.SubBoard.as_view()), name="sub_board"),
    url(r'^ajax/take_slip/$', login_required(ajax.SubSlipAjax.as_view()), name="take_slip"),
)
