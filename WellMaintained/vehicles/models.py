from django.db import models

from django.db import models

# from WellMaintained.accounts.models import Profile
from WellMaintained.branches.models import AutoPark


# TODO: add validators
class Vehicle(models.Model):
    MAX_LEN_REG_NUMBER = 8

    auto_park = models.ForeignKey(
        AutoPark,
        on_delete=models.CASCADE
    )

    # drivers = models.ForeignKey(
    #     Profile,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )

    reg_number = models.TextField(
        max_length=MAX_LEN_REG_NUMBER,
        unique=True,
        # primary_key=True,
        blank=False,
        null=False
    )

    # TODO: make model year dropdown menu auto complete from reg
    make = models.TextField(
        max_length=30,
        blank=False,
        null=False
    )

    model = models.TextField(
        max_length=30,
        blank=False,
        null=False
    )

    year = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    # TODO: add validator to max year
    mileage = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    colour = models.TextField(
        max_length=20,
        blank=False,
        null=False
    )

    # TODO: create categories as choises
    license_category = models.TextField(
        max_length=20,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True


class Car(Vehicle, models.Model):
    pass


class Van(Vehicle, models.Model):
    pass
