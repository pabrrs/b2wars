from django.test import TestCase
from django.conf import settings

from b2wars.apps.swapi.services import SwapiService


class SwapiServiceTestCase(TestCase):
    swapi = None
    planet = {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert"
    }
    films = [
        f"{settings.SWAPI_URL}/films/1/", 
        f"{settings.SWAPI_URL}/films/3/", 
        f"{settings.SWAPI_URL}/films/4/", 
        f"{settings.SWAPI_URL}/films/5/", 
        f"{settings.SWAPI_URL}/films/6/"
    ]


    def setUp(self):
        self.swapi = SwapiService()


    def test_get_planet_by_name(self):
        """ Tries to get planet by name """

        result = self.swapi.search_planet_by_name(
            self.planet['name']
        )
        self.assertEqual(result['name'], self.planet['name'])
        self.assertEqual(result['climate'], self.planet['climate'])
        self.assertEqual(result['terrain'], self.planet['terrain'])


    def test_get_films_from_planet(self):
        """ Check if films from planet are been returned """

        films_from_planet = self.swapi.get_films_from_planet(
            self.planet['name']
        )
        self.assertGreaterEqual(len(films_from_planet), len(self.films))
        self.assertTrue(
            any(self.films[0] == film_url for film_url in films_from_planet)
        )


    def tearDown(self):
        self.swapi = None
