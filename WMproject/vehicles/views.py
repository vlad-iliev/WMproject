from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from WMproject.vehicles.forms import AddCarForm,AddVanForm

@login_required
def add_vehicle(request):
    return redirect('add vehicle')
@login_required
def add_car(request):
    if request.method == 'GET':
        form = AddCarForm()
    else:
        form = AddCarForm(request.POST)
        if form.is_valid():
            form.save()
            #TODO: redirect to car catalogue
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'vehicle/car-create.html', context)


@login_required
def add_van(request):
    if request.method == 'GET':
        form = AddVanForm()
    else:
        form = AddCarForm(request.POST)
        if form.is_valid():
            form.save()
            #TODO: redirect to car catalogue
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'vehicle/van-create.html', context)
