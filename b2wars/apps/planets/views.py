from rest_framework import viewsets

from b2wars.apps.planets.models import Planet
from b2wars.apps.planets.serializers import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    """
    Planets API resource
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
