Deployment Guide
==============

This guide explains how to deploy the OC Lettings application to production environments.

CI/CD Pipeline
------------

The application uses GitHub Actions for continuous integration and deployment:

1. **Testing**: Runs automated tests and linting
2. **Docker Build**: Creates and pushes Docker image to Docker Hub
3. **Deployment**: Deploys the application to Render cloud platform

Configuration
-----------

GitHub Repository Secrets
~~~~~~~~~~~~~~~~~~~~~~~

The following secrets must be configured in your GitHub repository:

- `DOCKERHUB_USERNAME`: Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token
- `RENDER_API_KEY`: API key for Render
- `RENDER_SERVICE_ID`: Service ID from Render
- `DJANGO_SECRET_KEY`: Django secret key for production
- `SENTRY_DSN`: Sentry Data Source Name for error tracking

Environment Variables
~~~~~~~~~~~~~~~~~~

The application requires these environment variables:

.. code-block:: bash

   DJANGO_SECRET_KEY=your_production_secret_key
   SENTRY_DSN=your_sentry_dsn
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

Docker Deployment
--------------

Local Docker Run
~~~~~~~~~~~~~~

To run the application with Docker locally:

.. code-block:: bash

   docker build -t oc-lettings .
   docker run -p 8000:8000 --env-file .env oc-lettings

Docker Hub
~~~~~~~~

The Docker image is automatically pushed to Docker Hub when changes are merged to the main branch.

To pull and run the latest image manually:

.. code-block:: bash

   docker pull yourusername/oc-lettings:latest
   docker run -p 8000:8000 --env-file .env yourusername/oc-lettings:latest

Render Deployment
--------------

The application is configured to deploy automatically to Render when changes are pushed to the main branch.

Manual Deployment Steps
~~~~~~~~~~~~~~~~~~~~~

1. Log in to your Render dashboard
2. Navigate to your service
3. Click "Manual Deploy" and select "Deploy latest commit"
4. Monitor the build logs for any issues

Monitoring
---------

Sentry Integration
~~~~~~~~~~~~~~~

The application uses Sentry for error tracking and monitoring:

1. Errors are automatically captured and sent to Sentry
2. Login to the Sentry dashboard to view error reports
3. Configure alert rules to get notifications for critical errors

Post-Deployment Verification
-------------------------

After deploying, verify the following:

1. Application loads correctly at your domain
2. Static files (CSS, JavaScript) load properly
3. You can browse lettings and profiles
4. Admin interface works correctly
5. Sentry is capturing errors (test with /sentry-debug/ endpoint)
