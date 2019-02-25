release: python manage.py migrate --settings=b2wars.settings.heroku
release: python runtests.py
web: gunicorn b2wars.wsgi