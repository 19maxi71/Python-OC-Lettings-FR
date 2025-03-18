# OC Lettings

Orange County Lettings website - A Django property rental application.

## Useful Links

- [Deployed Application](https://python-oc-lettings-fr-92uw.onrender.com/)
- [Documentation](https://19maxi71python-oc-lettings-fr.readthedocs.io/en/latest/)
- [Docker Hub](https://hub.docker.com/r/19maxi71/oc-lettings)
- [CI/CD Pipeline](https://github.com/19maxi71/Python-OC-Lettings-FR/actions)

## Project Structure

The project is divided into three Django applications:
- **oc_lettings_site**: Main application and configuration
- **lettings**: Property and address management
- **profiles**: User profile management

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.9.x (3.9.0 to 3.9.18)

Note: More recent versions of Python might cause incompatibilities with some modules.

In the rest of the local development documentation, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step gives errors with package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm that the `python` command runs the Python interpreter in the virtual environment
`which python`
- Confirm that the Python interpreter version is 3.9.x `python --version`
- Confirm that the `pip` command runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm the site works and you can navigate (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Unit Tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a SQLite shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profile table, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profile table, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` to quit

#### Admin Panel

- Go to `http://localhost:8000/admin`
- Log in with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except:

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1`
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

### Error Tracking Setup

1. Create a Sentry account at https://sentry.io
2. Create a new project and get your DSN
3. Add your Sentry DSN to `.env` file
4. Test the setup:
   - Set DEBUG=False in .env
   - Visit: `http://localhost:8000/sentry-debug/`
   - Check your Sentry dashboard for the error

### Testing

Run the test suite:
```bash
python manage.py test
```

Test specific apps:
```bash
python manage.py test lettings
python manage.py test profiles
python manage.py test oc_lettings_site
```

### Error Pages
Custom error pages are available:
- 404 Not Found: `/test-404/`
- 500 Server Error: `/test-500/`

## Deployment

### Overview
The application uses a CI/CD pipeline with GitHub Actions that:
1. Runs tests and linting
2. Builds and pushes Docker image
3. Deploys to Render

### Requirements
- Docker account and CLI
- Render account
- Environment variables set in GitHub repository:
  - DOCKERHUB_USERNAME
  - DOCKERHUB_TOKEN
  - RENDER_API_KEY
  - RENDER_SERVICE_ID
  - Other Django environment variables

## Docker Deployment

### Building and Running with Docker

1. Build the Docker image:
```bash
docker build -t oc-lettings .
```

2. Run the container with environment variables from .env:
```bash
docker run -p 8000:8000 --env-file .env oc-lettings
```

3. Access the application at http://localhost:8000

### Pull from Docker Hub

You can also pull the pre-built image directly:
```bash
docker pull 19maxi71/oc-lettings:latest
docker run -p 8000:8000 --env-file .env 19maxi71/oc-lettings:latest
```

### Automated Deployment:
- Push to main branch triggers full pipeline
- Push to other branches only runs tests
- Monitor deployment status in GitHub Actions
This pipeline runs automatically on every push to the main branch.

### Environment Variables Required
```
DJANGO_SECRET_KEY=your_secret_key
SENTRY_DSN=your_sentry_dsn
DEBUG=False
ALLOWED_HOSTS=python-oc-lettings-fr-92uw.onrender.com,localhost,127.0.0.1
```

## Documentation

Complete project documentation is available on [Read the Docs.](https://19maxi71python-oc-lettings-fr.readthedocs.io/en/latest/)

To generate documentation locally:
```bash
cd docs
pip install -r requirements.txt
sphinx-build -b html source build
```
Then open docs/build/index.html in your browser.
