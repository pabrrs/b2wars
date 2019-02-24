from rest_framework import serializers

from b2wars.apps.planets.models import Planet

class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ('url', 'name', 'climate', 'terrain', 'created_at', 'updated_at')
