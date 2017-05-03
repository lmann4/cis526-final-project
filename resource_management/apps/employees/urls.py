from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^home/$', login_required(views.home), name="employee_home_redirect"),
    url(r'^(?P<pk>[\d]+)/$', login_required(views.EmployeeDetail.as_view()), name="employee_detail"),
)
