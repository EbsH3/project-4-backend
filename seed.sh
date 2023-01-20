#!/bin/bash

echo "dropping database django-h4cked"
dropdb django-h4cked

echo "creating database django-h4cked"
createdb django-h4cked

python manage.py makemigrations

python manage.py migrate

echo "inserting employers"
python manage.py loaddata employers/seeds.json

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting salaries"
python manage.py loaddata salaries/seeds.json

echo "inserting sectors"
python manage.py loaddata sectors/seeds.json

echo "inserting tips"
python manage.py loaddata tips/seeds.json

echo "inserting vacancies"
python manage.py loaddata vacancies/seeds.json

echo "inserting feedback"
python manage.py loaddata feedback/seeds.json