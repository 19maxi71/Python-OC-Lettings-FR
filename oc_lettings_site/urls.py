from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error, name='trigger_error'),  # For testing Sentry
    path('test-404/', views.test_404, name='test_404'),  # For testing 404 template
    path('test-500/', views.test_500, name='test_500'),  # For testing 500 template
]
