from django.db import models

from WellMaintained.accounts.models import Profile
from WellMaintained.branches.models import CompanyBranch


class Manager(models.Model):

    name = models.CharField(
        max_length=25,
        blank=False,
        null=False,
    )

    branch = models.ForeignKey(
        CompanyBranch,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    staff = models.ManyToManyField(
        Profile,
        blank=True,
    )