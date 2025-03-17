# Étape de construction
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Étape finale
FROM python:3.9-slim
WORKDIR /app

# Copier les dépendances installées
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copier le projet
COPY . .

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Configuration statique
RUN mkdir -p staticfiles
RUN python manage.py collectstatic --noinput --settings=oc_lettings_site.settings.prod

# Port d'exposition
EXPOSE 8000

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
