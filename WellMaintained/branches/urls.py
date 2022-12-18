from django.urls import path, include

from WellMaintained.branches.views import branches_view, branch_edit_view, BranchCreateView, branch_details_view, \
    branches_auto_park, DeleteBranchView

urlpatterns = (
    path('create/', BranchCreateView.as_view(), name='create branch'),
    path('', branches_view, name='list branch'),
    path('branch/<int:pk>/', include([
        path('details/', branch_details_view, name='details branch'),
        path('edit/', branch_edit_view, name='edit branch'),
        path('delete/', DeleteBranchView.as_view(), name='delete branch'),
        path('auto-park/', branches_auto_park, name='auto park')
    ])),
)
