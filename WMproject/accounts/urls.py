from django.urls import path, include

from WMproject.accounts.views import SignInView, SignUpView, SignOutView, \
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('signin/', SignInView.as_view(), name='sign in user'),
    path('signup/', SignUpView.as_view(), name='sign up user'),
    path('signout/', SignOutView.as_view(), name='sign out user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
