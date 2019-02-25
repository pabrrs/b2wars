# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from b2wars.settings.test import *

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('TRAVIS_DB_NAME'),
        'USER': os.environ.get('TRAVIS_DB_USER'),
        'PASSWORD': os.environ.get('TRAVIS_DB_PASSWORD'),
    }
}
