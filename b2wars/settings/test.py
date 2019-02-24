# Import Django RestFramework settings

# pylint: disable=unused-import
from b2wars.settings.base import REST_FRAMEWORK

DEBUG = True

SECRET_KEY = 'TEST-KEY'

INSTALLED_APPS = [
    'b2wars.apps.core',
    'b2wars.apps.planets',
    'b2wars.tests'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}
