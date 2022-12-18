from django import forms

from WellMaintained.accounts.models import Profile
from WellMaintained.vehicles.models import Car, Van, Vehicle


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class VanCreateForm(forms.ModelForm):
    class Meta:
        model = Van
        fields = '__all__'


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class VanEditForm(forms.ModelForm):
    class Meta:
        model = Van
        fields = '__all__'

class HireCarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('hired_cars',)


class VehicleReturnForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'