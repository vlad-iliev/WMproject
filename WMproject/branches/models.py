from django.db import models


class CompanyBranch(models.Model):
    MAX_LEN_NAME = 30
    # TODO: create location form
    # https://stackoverflow.com/questions/48388366/i-want-to-add-a-location-field-in-django-model-which-take-location-input-by-putt

    branch_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        blank=False,
        null=False,
    )

    staff_capacity = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    parking_capacity = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    taken_parking_spaces = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )