# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

# Set non-sensitive environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=oc_lettings_site.settings \
    STATIC_ROOT=/app/staticfiles

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create static files directory
RUN mkdir -p staticfiles

# Copy project files after installing all dependencies
COPY . .

# Create non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app

# Collect static files with a temporary key
RUN DJANGO_SECRET_KEY=temporary_key_for_collectstatic python manage.py collectstatic --noinput

# Build arguments with defaults
ARG DJANGO_SECRET_KEY=default_build_secret_key_not_for_production
ARG DEBUG=False
ARG ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Set environment variables from build args
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} \
    DEBUG=${DEBUG} \
    ALLOWED_HOSTS=${ALLOWED_HOSTS}

# Switch to non-root user
USER appuser

EXPOSE 8000

# Command to start the application
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
