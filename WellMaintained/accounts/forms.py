from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from WellMaintained.accounts.models import Profile
from WellMaintained.branches.models import CompanyBranch

UserModel = get_user_model()


# class SignUpForm(auth_forms.UserCreationForm):
#     BRANCH_OPTIONS = [(str(a),str(a))for a in CompanyBranch.objects.all()]
#     print(f'branches:{BRANCH_OPTIONS}')
#
#
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     # branch = forms.ChoiceField(choices=BRANCH_OPTIONS,)
#     age = forms.IntegerField()
#     gender = forms.CharField()
#
#     class Meta:
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age','gender')
#         field_classes = {'username': auth_forms.UsernameField}
#     # save with data for profile
#     def save(self, commit=True):
#         user = super().save(commit=commit)
#         profile = Profile(
#             first_name=self.cleaned_data['first_name'],
#             last_name=self.cleaned_data['last_name'],
#             age=self.cleaned_data['age'],
#             gender=self.cleaned_data['gender'],
#             # branch=CompanyBranch.objects.filter(branch_name=self.cleaned_data['branch']).get(),
#             user=user,
#
#         )
#         if commit:
#             profile.save()
#
#         return user
class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
        field_classes = {'username': auth_forms.UsernameField}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
