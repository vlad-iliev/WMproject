from django import forms

from WellMaintained.branches.models import CompanyBranch, AutoPark


class CreateBranchForm(forms.ModelForm):
    branch_name = forms.CharField()
    staff_capacity = forms.IntegerField()
    parking_capacity = forms.IntegerField()

    class Meta:
        model = CompanyBranch
        fields = '__all__'

    def save(self, commit=True):
        branch = super().save(commit=commit)

        auto_park = AutoPark(
            branch=branch,
            parking_capacity=self.cleaned_data['parking_capacity'],

        )
        if commit:
            auto_park.save()

        return branch


class EditBranchForm(forms.ModelForm):
    class Meta:
        model = CompanyBranch
        fields = '__all__'


class DeleteBranchForm(forms.ModelForm):
    class Meta:
        model=CompanyBranch
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            self.instance.delete()

        return self.instance
