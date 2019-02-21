# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
from b2wars.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': os.environ.get('B2WARS_DB_NAME'),
        'TEST_NAME': os.environ.get('B2WARS_DB_TEST_NAME'),
        'HOST': os.environ.get('B2WARS_DB_HOST'),
        'OPTIONS': {
            'replication': {
                'strategy_class': os.environ.get('B2WARS_DB_STRATEGY_CLASS', 'SimpleStrategy'),
                'replication_factor': os.environ.get('B2WARS_DB_REPLICANTION_FACTOR', 1)
            }
        }
    }
}