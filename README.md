# Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.9.x (3.9.0 à 3.9.18)

Note: Des versions plus récentes de Python peuvent causer des incompatibilités avec certains modules.

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

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


### Automated Deployment:
- Push to main branch triggers full pipeline
- Push to other branches only runs tests
- Monitor deployment status in GitHub Actions


### Environment Variables Required
```
DJANGO_SECRET_KEY=your_secret_key
SENTRY_DSN=your_sentry_dsn
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com,localhost,127.0.0.1
```
