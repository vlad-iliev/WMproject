from django.urls import path

from WMproject.common.views import index

urlpatterns = (
    path('', index, name='index'),

)
