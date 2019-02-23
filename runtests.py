#!/usr/bin/env python
import os
import sys
import coverage

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'b2wars.settings.test'
    django.setup()
    test_runner_class = get_runner(settings)
    runner = test_runner_class(verbosity=2, interactive=True, failfast=False)

    # Set coverage to b2wars app
    cov = coverage.Coverage(source=['b2wars'])
    cov.start()
    # Run tests
    failures = runner.run_tests([])
    cov.stop()
    cov.save()

    # Show report only when have not failures
    if not bool(failures):
        # Show report on terminal
        cov.report()
        # Save html report on htmlcov folder
        cov.html_report(directory='htmlcov')

    sys.exit(failures)
