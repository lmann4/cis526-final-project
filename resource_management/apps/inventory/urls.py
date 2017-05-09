from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    
    url(r'^$', login_required(views.InventoryList.as_view()), name="frozen"),
    url(r'^add$', login_required(views.createInventoryView.as_view()), name='post_new'),
    url(r'^(?P<pk>[\d]+)/$', login_required(views.InventoryDetail.as_view()), name='inventory_detail'),
)
