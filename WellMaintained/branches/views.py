from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.shortcuts import render, redirect
from django.views.generic import edit

from WellMaintained.branches.forms import CreateBranchForm, EditBranchForm
from WellMaintained.branches.models import CompanyBranch, AutoPark
from WellMaintained.branches.utils import count_staff_at_branch
from WellMaintained.common.decorators import superuser_only
from WellMaintained.vehicles.models import Car, Van


class BranchCreateView(LoginRequiredMixin, views.CreateView):
    form_class = CreateBranchForm
    template_name = 'branches/branch-create.html'
    success_url = reverse_lazy('list branch')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
@staff_member_required
def branch_details_view(request, pk):
    branch = CompanyBranch.objects.filter(pk=pk).get()
    staff = count_staff_at_branch(branch)
    context = {
        'branch': branch,
        'staff': staff,
    }

    return render(request, 'branches/branch-details.html', context)


@login_required
@staff_member_required
def branch_edit_view(request, pk):
    branch = CompanyBranch.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditBranchForm(instance=branch)
    else:
        form = EditBranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('details branch', pk=pk)

    context = {
        'form': form,
        'branch': branch,
    }

    return render(request, 'branches/branch-edit.html', context)


class DeleteBranchView(LoginRequiredMixin, edit.DeleteView):
    model = CompanyBranch
    success_url = reverse_lazy('list branch')
    template_name = "branches/branch-delete.html"

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
def branches_auto_park(request, pk):
    branch = CompanyBranch.objects.filter(pk=pk).get()
    auto_park = AutoPark.objects.filter(pk=pk).get()
    cars = Car.objects.all().filter(auto_park_id=auto_park)
    vans = Van.objects.all().filter(auto_park_id=auto_park)

    context = {
        'cars': cars,
        'vans': vans,
        'branch': branch
    }

    return render(request, 'branches/auto_park.html', context)


@login_required
def branches_view(request):
    branches = CompanyBranch.objects.all()

    context = {
        'branches': branches,
    }

    return render(request, 'branches/branches-list.html', context)
