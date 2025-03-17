# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

# Set non-sensitive environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=oc_lettings_site.settings \
    DEBUG=False \
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

# Copy project files after installing dependencies
COPY . .

# Create non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Collect static files with a safe temporary key
USER root
RUN DJANGO_SECRET_KEY=temporary_key_for_collectstatic python manage.py collectstatic --noinput
USER appuser

# Accept build arguments
ARG DJANGO_SECRET_KEY
ARG DEBUG
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV DEBUG=${DEBUG}

EXPOSE 8000

# Use environment variable for secret key at runtime
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
