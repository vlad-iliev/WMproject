from django.urls import path, include

from WellMaintained.manager.views import ManagerCreateView, managers_list_view, ManagerDetailsView

urlpatterns = [
    path('list/',managers_list_view,name='manager list'),
    path('create/',ManagerCreateView.as_view(),name='create manager'),
    path('<int:pk>/', include([
        path('details/',ManagerDetailsView.as_view(),name='details manager')
    ]))
]