FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput || echo "Static files not collected"

# Use the correct WSGI module - with proper spacing between arguments
ENTRYPOINT ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
