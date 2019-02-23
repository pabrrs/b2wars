
DEBUG = True

SECRET_KEY = 'TEST-KEY'

INSTALLED_APPS = [
    'b2wars.tests'
]

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=b2wars.apps',
#     '--cover-tests',
#     '--cover-html',
#     '--cover-html-dir=htmlcov'
# ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}