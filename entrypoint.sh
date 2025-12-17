#!/bin/sh
set -e

# If using an external DB (Postgres) you can wait for it with the SQL_HOST/SQL_PORT env vars
if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for Postgres at $SQL_HOST:$SQL_PORT..."
  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 1
  done
fi

# Run migrations and collectstatic (no input)
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

# Allow passing a custom command (exec "gunicorn ..." by default)
exec "$@"
