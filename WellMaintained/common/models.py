from django.db import models


class DrivingLicence(models.Model):
    MAX_LEN_NUMBER = 15

    number = models.TextField(
        max_length=MAX_LEN_NUMBER,
        blank=False,
        null=False
    )
    # TODO: using template-filter date and a format e.g: {{ obj.created_at|date:'%y %m' }}.
    expiry_date = models.DateField()

    # TODO: make this into choises field
    categories = models.TextField(
        max_length=2,
        blank=False,
        null=False
    )