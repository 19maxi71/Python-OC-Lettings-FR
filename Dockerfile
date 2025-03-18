# Build stage
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

# Environment variables with defaults that can be overridden at build time
ARG DJANGO_SECRET_KEY
ARG SENTRY_DSN
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV SENTRY_DSN=${SENTRY_DSN}
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBUG=False

RUN mkdir -p staticfiles
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Health check to ensure the container is running properly
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
