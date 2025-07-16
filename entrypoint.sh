#!/bin/sh

# Wait for the PostgreSQL database to be ready
# The 'db' here refers to the service name in your docker-compose.yml
# The '5432' is the default PostgreSQL port
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Execute the main command (Django's runserver or Gunicorn)
exec "$@"