from django.urls import path, include
from WellMaintained.vehicles.views import add_car, vehicle_details_view, vehicle_edit_view, vehicle_hire_view, \
    DeleteVehicleView, vehicle_return_view

urlpatterns = (
    path('<int:pk>/delete/', DeleteVehicleView.as_view(), name='delete vehicle'),
    path('vehicle/<str:reg_number>/',include([
        path('details/',vehicle_details_view, name='detail vehicle'),
        path('hire/', vehicle_hire_view, name='hire vehicle'),
        path('return/', vehicle_return_view, name='return vehicle'),
        path('edit/',vehicle_edit_view, name='edit vehicle'),

    ])),
    path('add/', include([
        path('car/', add_car, name='add car'),
    ])),
)
