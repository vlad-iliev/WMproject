from django.urls import path, include

from WellMaintained.accounts.views import SignInView, SignUpView, SignOutView, \
    UserDetailsView, UserEditView, UserDeleteView, create_profile, hired_cars_list

urlpatterns = (
    path('signin/', SignInView.as_view(), name='sign in user'),
    path('signup/', SignUpView.as_view(), name='sign up user'),
    path('signout/', SignOutView.as_view(), name='sign out user'),
    path('accounts/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('create/', create_profile, name='create accounts'),
        path('hired-cars/', hired_cars_list, name='hired cars accounts'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
