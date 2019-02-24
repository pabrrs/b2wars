from django.test import TestCase

from b2wars.apps.swapi.services import SwapiService


class SwapiServiceTestCase(TestCase):
    swapi = None

    planet = {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert"
    }

    films = [
        {
            "name": "Attack of the Clones",
            "url": "https://swapi.co/api/films/5/"
        },
        {
            "name": "The Phantom Menace",
            "url": "https://swapi.co/api/films/4/"
        },
        {
            "name": "Revenge of the Sith",
            "url": "https://swapi.co/api/films/6/"
        },
        {
            "name": "Return of the Jedi",
            "url": "https://swapi.co/api/films/3/"
        },
        {
            "name": "A New Hope",
            "url": "https://swapi.co/api/films/1/"
        }
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

        films = self.swapi.get_films_from_planet(
            self.planet['name']
        )

        self.assertGreaterEqual(len(films), len(self.films))

    def tearDown(self):
        self.swapi = None
