from django.urls import path, include

from rest_framework import routers
from b2wars.apps.planets.viewsets import PlanetViewSet

router = routers.DefaultRouter()
router.register(r'planets', PlanetViewSet)

urlpatterns = [

    # Automatic URL mapping for registered resources
    path('', include(router.urls)),
]
