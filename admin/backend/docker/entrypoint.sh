#!/bin/bash

set -e

python manage.py wait_for_db
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@" 