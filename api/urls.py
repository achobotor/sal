from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^machines/(?P<serial>.+)/inventory/$', views.MachineInventory.as_view()),
    url(r'^machines/(?P<serial>.+)/full/$', views.MachineFullDetail.as_view()),
    url(r'^machines/(?P<serial>.+)/$', views.MachineDetail.as_view()),
    url(r'^machines/$', views.MachineList.as_view()),
    url(r'^facts/(?P<serial>.+)/$', views.Facts.as_view()),
    url(r'^conditions/(?P<serial>.+)/$', views.Conditions.as_view()),
    url(r'^pending_apple_updates/(?P<serial>.+)/$', views.PendingAppleUpdates.as_view()),
    url(r'^pending_updates/(?P<serial>.+)/$', views.PendingUpdates.as_view()),
    url(r'^business_units/(?P<pk>.+)/$', views.BusinessUnitView.as_view()),
    url(r'^business_units/$', views.BusinessUnitList.as_view()),
    url(r'^machine_groups/(?P<pk>.+)/$', views.MachineGroupView.as_view()),
    url(r'^machine_groups/$', views.MachineGroupList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
