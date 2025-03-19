Quick Start Guide
================

Once you have installed the application, follow these steps to get started.

Running the Development Server
-----------------------------

1. Make sure your virtual environment is activated:

   .. code-block:: bash

      source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Start the development server:

   .. code-block:: bash

      python manage.py runserver

3. Visit http://localhost:8000 in your browser.

Accessing the Admin Interface
----------------------------

1. Go to http://localhost:8000/admin/
2. Login with your superuser credentials.
3. From here you can:
   - Manage property listings
   - Add or modify user profiles
   - Control application settings

Key URLs
--------

- **Home Page**: http://localhost:8000/
- **Lettings List**: http://localhost:8000/lettings/
- **Profiles List**: http://localhost:8000/profiles/
- **Admin Interface**: http://localhost:8000/admin/

Testing
-------

Run tests to ensure everything is working properly:

.. code-block:: bash

   python manage.py test

Code Quality
-----------

Check code quality with flake8:

.. code-block:: bash

   flake8
