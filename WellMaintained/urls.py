from django.contrib import admin
from django.urls import path, include
# from WellMaintained.accounts.admin import app_user_admin_site

urlpatterns = [
    # path('user_admin/', app_user_admin_site.urls),
    path('admin/', admin.site.urls),
    path('accounts/',include('WellMaintained.accounts.urls')),
    path('vehicles/',include('WellMaintained.vehicles.urls')),
    path('manager/',include('WellMaintained.manager.urls')),
    path('',include('WellMaintained.common.urls')),
    path('branches/',include('WellMaintained.branches.urls')),
]

# Vv123AA321