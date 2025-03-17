from django.shortcuts import render
from django.http import Http404
import logging

logger = logging.getLogger('django')


def index(request):
    """
    Displays the home page.
    """
    try:
        logger.info('Accessing home page')
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f'Error rendering home page: {str(e)}')
        return handler500(request)


def handler404(request, exception):
    """
    Custom 404 page
    """
    logger.warning(f'Page not found: {request.path}')
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom 500 page
    """
    logger.error('Server error occurred')
    return render(request, '500.html', status=500)


def trigger_error(request):
    """
    Triggers a division by zero error.
    For testing Sentry.
    """
    division_by_zero = 1 / 0
    return None


def test_404(request):
    """
    View to test 404 template
    """
    logger.info('Testing 404 error page')
    raise Http404("Testing 404 page")


def test_500(request):
    """
    View to test 500 template
    """
    logger.info('Testing 500 error page')
    return render(request, '500.html', status=500, context={'error_message': 'Testing 500 page'})
