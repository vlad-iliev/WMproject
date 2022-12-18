from WellMaintained.accounts.models import Profile


def get_full_name_by_profile(profile: Profile):
    return ' '.join((profile.first_name, profile.last_name))
