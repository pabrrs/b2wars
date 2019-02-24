import json
import requests

from django.conf import settings

from b2wars.apps.swapi.exceptions import SwapiServiceError

class SwapiService:
    """ SWAPI service to read Star Wars API """

    @classmethod
    def search_planet_by_name(cls, name):
        """
        Search a planet by name in SWAPI and return the first match
        """

        url = "%s?search=%s" % (settings.SWAPI_PLANETS_URL, name)
        response = requests.get(url)
        if response.ok:
            return next(iter(json.loads(response.text)['results']), None)

        raise SwapiServiceError("SWAPI communitation error")

    @classmethod
    def get_films_from_planet(cls, planet_name):
        """ Return all films from planet """

        planet = cls.search_planet_by_name(planet_name)
        return planet.get('films', [])
