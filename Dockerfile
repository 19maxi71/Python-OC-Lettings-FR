FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Make sure static directory exists
RUN mkdir -p staticfiles

# Use ARG for build-time secret (not stored in final image metadata)
ARG BUILD_SECRET_KEY=dummy_key_for_collectstatic_only
RUN DJANGO_SECRET_KEY=${BUILD_SECRET_KEY} python manage.py collectstatic --noinput

# Run on port 8000
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
