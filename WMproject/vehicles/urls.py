from django.urls import path, include
from WMproject.vehicles.views import add_vehicle, add_car, add_van

urlpatterns = (
    path('add/', include([
        path('', add_vehicle, name='add vehicle'),
        path('car/', add_car, name='add car'),
        path('van/', add_van, name='add van'),
    ])),
)
