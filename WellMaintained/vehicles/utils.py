from django.contrib.auth import get_user_model

from WellMaintained.accounts.models import AppUser, Profile
from WellMaintained.vehicles.models import Car, Van

UserModel = get_user_model

def get_cars_by_profile_id(id):
    return Car.objects.filter(drivers=id).get()

def get_vehicle_by_reg(reg):
    if Car.objects.filter(reg_number=reg).exists():
        vehicle = Car.objects.filter(reg_number=reg).get()
    else:
        vehicle = Van.objects.filter(reg_number=reg).get()

    return vehicle

def get_user_by_id(user_id):
    return UserModel.objects.filter(id=user_id).get()

def get_profile_by_pk(pk):
    return Profile.objects.filter(pk=pk).get()
