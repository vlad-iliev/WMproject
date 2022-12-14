from django.db import models

from WMproject.accounts.models import AppUser


class DrivingLicense(models.Model):
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


class Message(models.Model):
    MAX_TEXT_LENGTH = 300

    user = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )
