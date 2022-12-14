from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from WMproject.accounts.forms import SignUpForm
from WMproject.accounts.models import Profile, AppUser
from WMproject.accounts.utils import get_full_name_by_profile

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'profile/profile-create.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in, after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'profile/profile-sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'profile/profile-sign-in.html'
    success_url = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'profile/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.object
        user_pk = self.object.pk
        profile = Profile.objects.filter(user_id=user_pk).get()

        context['email'] = email
        context['age'] = profile.age
        context['gender'] = profile.gender
        context['full_name'] = get_full_name_by_profile(profile)

        context['pk'] = user_pk
        # TODO: continue with the context based on HTML
        return context


class UserEditView(views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = Profile
    fields = ('__all__')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
