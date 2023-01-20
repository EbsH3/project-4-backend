#!/bin/bash

echo "creating employers/seeds.json"
python manage.py dumpdata employers --output employers/seeds.json --indent=2;

echo "creating salaries/seeds.json"
python manage.py dumpdata salaries --output salaries/seeds.json --indent=2;

echo "creating sectors/seeds.json"
python manage.py dumpdata sectors --output sectors/seeds.json --indent=2;

echo "creating tips/seeds.json"
python manage.py dumpdata tips --output tips/seeds.json --indent=2;

echo "creating feedback/seeds.json"
python manage.py dumpdata feedback --output feedback/seeds.json --indent=2;

echo "creating vacancies/seeds.json"
python manage.py dumpdata vacancies --output vacancies/seeds.json --indent=2;


echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;