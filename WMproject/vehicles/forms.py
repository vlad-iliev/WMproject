from django import forms
from WMproject.vehicles.models import Vehicle


class VehicleBaseForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class AddCarForm(VehicleBaseForm):
    pass


class AddVanForm(VehicleBaseForm):
    pass
