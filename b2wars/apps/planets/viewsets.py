from rest_framework import viewsets

from b2wars.apps.planets.models import Planet
from b2wars.apps.planets.serializers import PlanetSerializer
from b2wars.apps.planets.filters import PlanetFilter

# pylint: disable=too-many-ancestors
class PlanetViewSet(viewsets.ModelViewSet):
    """
    Planets API resource

    retrieve:
        Get a planet object.

    list:
        List all planet.

    create:
        Create a planet.

    update:
        Update all fields on a planet object.

    partial_update:
        Update one or more fields on an planet object.

    delete:
        Delete a planet.
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_class = PlanetFilter
