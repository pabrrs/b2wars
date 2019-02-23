from datetime import datetime
from django.test import TestCase

from b2wars.tests.models import TimeStampedMock

class MixinsTestCase(TestCase):

    def setUp(self):
        self.tsm_instance = TimeStampedMock.objects.create() 

    def test_model_has_craeted_at_updated_at_fields(self):
        """
        Check if fields `created_at` and `updated_at` was implemented in subclass
        """
        self.assertTrue(hasattr(TimeStampedMock, 'created_at'))
        self.assertTrue(hasattr(TimeStampedMock, 'updated_at'))

        self.assertEqual(type(self.tsm_instance.created_at), datetime)
        self.assertEqual(type(self.tsm_instance.updated_at), datetime)


    def test_created_at_value_on_add(self):
        """
        Check current datetime on `created_at` when edit instance
        """
        self.assertIsNotNone(self.tsm_instance.created_at)
        self.assertLess(self.tsm_instance.created_at, datetime.now())


    def test_updated_value_on_edit(self):
        """
        Check current datetime on `updated_at` when edit instance
        """
        self.assertIsNotNone(self.tsm_instance.updated_at)

        self.tsm_instance.save()

        self.assertGreater(
            self.tsm_instance.updated_at, 
            self.tsm_instance.created_at
        )

    def tearDown(self):
        self.tsm_instance.delete()
