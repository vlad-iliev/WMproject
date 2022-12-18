from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import edit

from WellMaintained.accounts.models import Profile
from WellMaintained.common.decorators import allow_groups
from WellMaintained.vehicles.forms import CarCreateForm, CarEditForm, VanEditForm, HireCarForm, \
    VehicleReturnForm
from WellMaintained.vehicles.models import Car
from WellMaintained.vehicles.utils import get_vehicle_by_reg, get_profile_by_pk


@login_required
@staff_member_required
def add_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'vehicle/car-create.html', context)


@login_required
def vehicle_details_view(request, reg_number):
    vehicle = get_vehicle_by_reg(reg_number)
    context = {
        'vehicle': vehicle,
    }

    return render(request, 'vehicle/car-details.html', context)


@login_required
@staff_member_required
def vehicle_edit_view(request, reg_number):
    vehicle = get_vehicle_by_reg(reg_number)
    if isinstance(vehicle, Car):
        get_form = CarEditForm(instance=vehicle)
        post_form = CarEditForm(request.POST, instance=vehicle)
    else:
        get_form = VanEditForm(instance=vehicle)
        post_form = VanEditForm(request.POST, instance=vehicle)

    if request.method == 'GET':
        form = get_form
    else:
        form = post_form
        if form.is_valid():
            form.save()
            return redirect('detail vehicle', reg_number=reg_number)

    context = {
        'form': form,
        'vehicle': vehicle,
    }

    return render(request, 'vehicle/car-edit.html', context)


@login_required
def vehicle_hire_view(request, reg_number):
    vehicle = get_vehicle_by_reg(reg_number)
    profile = get_profile_by_pk(request.user.id)

    if request.method == 'GET':
        form = HireCarForm(instance=profile)
    else:
        form = HireCarForm(request.POST, instance=profile)
        if form.is_valid():
            profile.hired_cars.add(Car.objects.get(pk=vehicle.pk))
            return redirect('index')

    context = {
        'form': form,
        'vehicle': vehicle,
        'profile': profile,
    }

    return render(request, 'vehicle/vehicle-hire.html', context)


@login_required
def vehicle_return_view(request, reg_number):
    vehicle = get_vehicle_by_reg(reg_number)
    profile = get_profile_by_pk(request.user.id)

    get_form = VehicleReturnForm(instance=vehicle)
    post_form = VehicleReturnForm(request.POST, instance=vehicle)

    if request.method == 'GET':
        form = get_form
    else:
        form = post_form
        if form.is_valid():
            form.save()
            profile.hired_cars.remove(Car.objects.filter(id=vehicle.id).get())
            return redirect('hired cars profile', pk=request.user.pk)

    context = {
        'form': form,
        'vehicle': vehicle,
    }

    return render(request, 'vehicle/vehicle-return.html', context)


class YourVehicles(LoginRequiredMixin, views.ListView):
    template_name = 'vehicle/your_vehicles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        profile = Profile.objects.filter(id=self.kwargs['pk'])


class DeleteVehicleView(LoginRequiredMixin, edit.DeleteView):
    allow_groups(['Directors'])
    model = Car
    success_url = reverse_lazy('index')
    template_name = "vehicle/car-delete.html"

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args,**kwargs)
