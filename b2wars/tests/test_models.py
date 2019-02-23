from django.test import TestCase

from b2wars.apps.planets.models import Planet

class PlanetTestCase(TestCase):

    def test_create_planet(self):
        """ Tries to create a planet """
        planet = Planet.objects.create(
            name="Alderaan",
            climate="temperate",
            terrain="grasslands, mountains"
        )

        self.assertEqual(Planet.objects.last().id, planet.id)


    def test_update_planet(self):
        """ Tries to update a planet """
        planet = Planet.objects.create(
            name="Dagobah",
            climate="murky",
            terrain="plain"
        )

        planet.terrain = "swamp, jungle"
        planet.save()

        self.assertEqual(Planet.objects.last().terrain, planet.terrain)


    def test_delete_planet(self):
        """ Tries to delete a planet """
        planet = Planet.objects.create(
            name="Dagobah",
            climate="murky",
            terrain="plain"
        )

        planet.delete()

        self.assertNotIn(
            planet,
            Planet.objects.all()
        )
