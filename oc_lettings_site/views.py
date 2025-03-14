from django.shortcuts import render


def index(request):
    """
    Displays the home page.
    """
    return render(request, 'index.html')


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, '500.html', status=500)
