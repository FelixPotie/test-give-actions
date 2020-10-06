from rest_framework import routers
from django.urls import include, path

from .views import CampagneViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'campagnes', CampagneViewSet)
router.register(r'tags', TagViewSet)

urlpatterns =[
    path('', include(router.urls)),
]