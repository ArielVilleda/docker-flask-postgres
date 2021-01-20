#!/bin/sh

# Applying-Checking migrations
python manage.py db upgrade

# Importing postal_codes to DB
python manage.py postal_codes

if [ $FLASK_ENV = "test" -o $FLASK_ENV = "dev" ];
then
    echo "NOT DEPLOYED ENVIROMENT" 
    echo "Access to the container and use <python manage.py run> instead"
    echo "Keeping container alive..."
    while true; do sleep 1; done
else
    echo "Starting gunicorn server for PRODUCTION ENVIROMENT" 
    gunicorn --bind 0:5000 --workers 2 manage:app
fi
