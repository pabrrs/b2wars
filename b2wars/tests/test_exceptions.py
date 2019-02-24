from django.test import TestCase

from b2wars.apps.swapi.exceptions import SwapiServiceError

class SwapiServiceTestCase(TestCase):

    def test_exception_class(self):
        """ Check SwapiServiceError parent class """

        self.assertTrue(issubclass(SwapiServiceError, Exception))
