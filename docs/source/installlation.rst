Installation Guide
================

Prerequisites
------------
* Python 3.9+
* Docker (optional for containerization)
* Git

Local Installation
-----------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/oc-lettings.git
      cd oc-lettings

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Configure environment:

   Create a `.env` file in the project root with:

   .. code-block:: bash

      DJANGO_SECRET_KEY=your_secret_key
      SENTRY_DSN=your_sentry_dsn
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1

5. Run migrations:

   .. code-block:: bash

      python manage.py migrate

6. Create a superuser (optional):

   .. code-block:: bash

      python manage.py createsuperuser

Docker Installation
------------------

1. Build Docker image:

   .. code-block:: bash

      docker build -t oc-lettings .

2. Run with environment variables:

   .. code-block:: bash

      docker run -p 8000:8000 --env-file .env oc-lettings
