from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WMproject.common.urls')),
    path('accounts/', include('WMproject.accounts.urls')),
    path('vehicles/', include('WMproject.vehicles.urls')),
    path('branches/', include('WMproject.branches.urls')),
]


#Vv123AA321