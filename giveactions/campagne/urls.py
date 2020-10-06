from rest_framework import routers
from django.urls import include, path

from .views import CampagneViewSet

router = routers.DefaultRouter()
router.register(r'campagnes', CampagneViewSet, basename='campagne')

urlpatterns =[
    path('', include(router.urls)),
]