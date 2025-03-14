from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from oc_lettings_site.views import handler500
from .models import Profile
import logging

logger = logging.getLogger('django')


def index(request):
    """
    Displays the list of user profiles.
    """
    try:
        logger.info('Accessing profiles index page')
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f'Error accessing profiles index: {str(e)}')
        return handler500(request)


def profile(request, username):
    """
    Displays the details of a specific user profile.
    """
    try:
        logger.info(f'Accessing profile details for username: {username}')
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except ObjectDoesNotExist:
        logger.warning(f'Profile not found for username: {username}')
        raise Http404(f"Profile for {username} does not exist")
    except Exception as e:
        logger.error(f'Error accessing profile {username}: {str(e)}')
        return handler500(request)
