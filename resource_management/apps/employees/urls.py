from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^(?P<pk>[\d]+)/$', login_required(views.EmployeeDetail.as_view()), name="employee_detail"),
)
