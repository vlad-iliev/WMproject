from django.urls import path

from WellMaintained.common.views import index

urlpatterns = (
    path('',index,name='index'),
)