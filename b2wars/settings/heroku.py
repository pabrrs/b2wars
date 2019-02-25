# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from b2wars.settings.dev import *

# MongoDB container connection
# see docker-compose.yml

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': os.environ.get('B2WARS_HEROKU_DB_NAME'),
#         'HOST': os.environ.get('B2WARS_HEROKU_DB_HOST'),
#         'USER': os.environ.get('B2WARS_HEROKU_DB_USER'),
#         'PORT': int(os.environ.get('B2WARS_HEROKU_DB_PORT')),
#         'PASSWORD': os.environ.get('B2WARS_HEROKU_DB_PASSWORD'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'heroku_0lhl3p2z',
        'HOST': 'ds149875.mlab.com',
        'USER': 'heroku_0lhl3p2z',
        'PORT': 49875,
        'PASSWORD': 'klqct85ltut5vi6v4n9jomd7hk',
    }
}
