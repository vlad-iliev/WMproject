from django import forms

from WellMaintained.manager.models import Manager


class ManagerCreateForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'