#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

## DB 생성
python manage.py create_db
## Wanted Data Insert
python manage.py insert_wanted

exec "$@"
