Project Overview
===============

OC Lettings is a Django web application for property rentals. The platform connects property owners with potential tenants, providing a simple and intuitive interface for browsing, searching, and managing property listings.

Key Features
-----------

* Browse available property listings
* View detailed information about properties
* Explore user profiles
* Admin interface for managing listings and users
* Error tracking and monitoring

Architecture
-----------

The application follows a standard Django architecture:

* **Front-end**: Django templates with Bootstrap CSS
* **Back-end**: Django views and models
* **Database**: SQLite (development) / PostgreSQL (production)
* **Monitoring**: Sentry for error tracking
* **Deployment**: Docker containerization with CI/CD pipeline
* **Hosting**: Render cloud platform

The codebase is organized into three main Django apps:

1. **oc_lettings_site**: Core functionality and base templates
2. **lettings**: Property listings management
3. **profiles**: User profile management
