from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from WellMaintained.accounts.managers import AppUserManager
from WellMaintained.branches.models import CompanyBranch
from WellMaintained.common.models import DrivingLicence
from WellMaintained.vehicles.models import Car


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False
    )

    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()


class Profile(models.Model):


    MIN_AGE = 18
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    branch = models.ForeignKey(
        CompanyBranch,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    hired_cars = models.ManyToManyField(
        Car,
        blank=True,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
        ),
        blank=False,
        null=False
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
        ),
        blank=False,
        null=False
    )

    age = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
        blank=False,
        null=False,
    )
    # TODO: make gender choices field
    gender = models.TextField(
        max_length=23
    )

    # TODO: add cloudinary accounts picture


#    photo = cloudinary_models.CloudinaryField(
#         null=False,
#         blank=True,

class Driver(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    driving_licence = models.OneToOneField(
        DrivingLicence,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
