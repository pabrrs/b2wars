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
        'PASSWORD': os.environ.get('B2WARS_HEROKU_DB_PASSWORD'),
        'PORT': 49875,
        'AUTH_MECHANISM': 'SCRAM-SHA-1', # Mechanism to authenticate in mLab Heroku Addon
    }
}
