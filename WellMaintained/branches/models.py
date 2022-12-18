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

    def __str__(self):
        return self.branch_name


class AutoPark(models.Model):
    branch = models.OneToOneField(
        CompanyBranch,
        primary_key=True,
        on_delete=models.CASCADE
    )

    parking_capacity = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.branch.branch_name

