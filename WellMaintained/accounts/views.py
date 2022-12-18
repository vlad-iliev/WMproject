from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from WellMaintained.accounts.forms import SignUpForm, ProfileCreateForm
from WellMaintained.accounts.models import Profile
from WellMaintained.accounts.utils import get_full_name_by_profile

from WellMaintained.vehicles.utils import get_profile_by_pk

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'profile/user-create.html'
    form_class = SignUpForm

    def get_success_url(self):
        success_url = reverse('create profile',kwargs={ 'pk':self.object.pk,})
        return success_url

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


@login_required
def create_profile(request, pk):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()

            return redirect('details user', pk=profile.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/profile-create.html',
        context,
    )


class SignInView(auth_views.LoginView):
    template_name = 'profile/profile-sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'profile/profile-sign-in.html'
    success_url = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
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
        context['branch'] = profile.branch
        context['full_name'] = get_full_name_by_profile(profile)

        context['pk'] = user_pk
        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = Profile
    fields = ('__all__',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


@login_required
def hired_cars_list(request, pk):
    profile = get_profile_by_pk(pk)
    hired_cars = profile.hired_cars.all()

    context = {
        'profile': profile,
        'hired_cars': hired_cars,
    }
    return render(request, 'profile/profile-hired-cars.html', context)
