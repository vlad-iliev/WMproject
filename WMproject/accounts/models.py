from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _

from WMproject.accounts.managers import AppUserManager


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

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,

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

    gender = models.TextField(
        max_length=23,
    )
    # gender = models.CharField(
    #     max_length=6,
    #     choices=GenderChoices.choices,
    #     default='OTHER',
    #     blank=False,
    #     null=False,
    # )

    # TODO: add cloudinary profile picture
#    photo = cloudinary_models.CloudinaryField(
#         null=False,
#         blank=True,
