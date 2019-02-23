#!/usr/bin/env python

import sys
import django
from django.conf import settings
from django.test.utils import get_runner


def configure():
    settings.configure(
        INSTALLED_APPS=(
            'django_nose',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        TEST_RUNNER='django_nose.NoseTestSuiteRunner',
        NOSE_ARGS=[
            '--with-coverage',
            '--cover-package=b2wars'
        ]
    )


def runtests():
    django.setup()
    test_runner_class = get_runner(settings)
    runner = test_runner_class(verbosity=2, interactive=True, failfast=False)
    failures = runner.run_tests(['b2wars', ])
    sys.exit(failures)


if __name__ == '__main__':
    configure()
    runtests()
