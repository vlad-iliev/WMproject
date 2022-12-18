from WellMaintained.accounts.models import Profile
from WellMaintained.branches.models import CompanyBranch, AutoPark


def count_staff_at_branch(branch):
    staff = Profile.objects.filter(branch=branch).count()
    return staff
