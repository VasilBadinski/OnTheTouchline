from django.shortcuts import render, get_object_or_404
from accounts.models import Profile
from core.models import Leagues


def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
    else:
        profile = None

    return {'profile': profile}

def leagues_processor(request):
    return {
        'leagues': Leagues.objects.all()
    }
