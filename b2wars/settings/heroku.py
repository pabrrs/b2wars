# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from b2wars.settings.dev import *

# MongoDB container connection
# see docker-compose.yml

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('B2WARS_HEROKU_DB_NAME'),
        'HOST': os.environ.get('B2WARS_HEROKU_DB_HOST'),
        'USER': os.environ.get('B2WARS_HEROKU_DB_USER'),
        'PORT': os.environ.get('B2WARS_HEROKU_DB_PORT'),
        'PASSWORD': os.environ.get('B2WARS_HEROKU_DB_PASSWORD'),
    }
}
