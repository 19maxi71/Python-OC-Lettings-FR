from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from oc_lettings_site.views import handler500
import logging

from .models import Letting

logger = logging.getLogger('django')


def index(request):
    """
    Displays the list of available lettings.
    """
    try:
        logger.info('Accessing lettings index page')
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f'Error accessing lettings index: {str(e)}')
        return handler500(request)


def letting(request, letting_id):
    """
    Displays the details of a specific letting.
    """
    try:
        logger.info(f'Accessing letting details for ID: {letting_id}')
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except ObjectDoesNotExist:
        logger.warning(f'Letting not found with ID: {letting_id}')
        raise Http404(f"Letting {letting_id} does not exist")
    except Exception as e:
        logger.error(f'Error accessing letting {letting_id}: {str(e)}')
        return handler500(request)
