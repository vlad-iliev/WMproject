from django.db import models


class Vehicle(models.Model):
    MAX_LEN_REG_NUMBER = 7

    reg_number = models.TextField(
        max_length=MAX_LEN_REG_NUMBER,
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


class Maintenance(models.Model):
    SMALL_SERVICE_DEFAULT = 100
    MEDIUM_SERVICE_DEFAULT = 250
    MAJOR_SERVICE_DEFAULT = 500

    fuel_consumption = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    fuel_tank_capacity = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    small_service_cost = models.PositiveIntegerField(
        default=SMALL_SERVICE_DEFAULT,
        blank=False,
        null=False,
    )

    medium_service_cost = models.PositiveIntegerField(
        default=MEDIUM_SERVICE_DEFAULT,
        blank=False,
        null=False,
    )

    major_service_cost = models.PositiveIntegerField(
        default=MAJOR_SERVICE_DEFAULT,
        blank=False,
        null=False,
    )


class Car(Vehicle, Maintenance, models.Model):
    pass


class Van(Vehicle, Maintenance, models.Model):
    pass
