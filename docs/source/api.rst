API Documentation
================

OC Lettings provides several interfaces for developers to interact with the application.

Views and URLs
-------------

Main URLs
~~~~~~~~~

.. code-block:: python

   urlpatterns = [
       path('', views.index, name='index'),
       path('lettings/', include('lettings.urls')),
       path('profiles/', include('profiles.urls')),
       path('admin/', admin.site.urls),
   ]

Lettings API
~~~~~~~~~~~

**List View**

- URL: `/lettings/`
- Function: `lettings.views.index`
- Description: Lists all available properties
- Returns: HTML page with all lettings

**Detail View**

- URL: `/lettings/<int:letting_id>/`
- Function: `lettings.views.letting`
- Description: Shows details for a specific property
- Parameters: `letting_id` (integer)
- Returns: HTML page with property details

Profiles API
~~~~~~~~~~~

**List View**

- URL: `/profiles/`
- Function: `profiles.views.index`
- Description: Lists all user profiles
- Returns: HTML page with all profiles

**Detail View**

- URL: `/profiles/<str:username>/`
- Function: `profiles.views.profile`
- Description: Shows details for a specific user profile
- Parameters: `username` (string)
- Returns: HTML page with profile details

Error Handling
-------------

**404 Handler**

- Function: `oc_lettings_site.views.handler404`
- Description: Custom 404 page for resource not found errors

**500 Handler**

- Function: `oc_lettings_site.views.handler500`
- Description: Custom 500 page for server errors

**Sentry Integration**

- URL: `/sentry-debug/`
- Function: `oc_lettings_site.views.trigger_error`
- Description: Deliberately triggers an error to test Sentry integration
- Note: For development and testing purposes only
