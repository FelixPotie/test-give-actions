from rest_framework import routers
from django.urls import include, path

from .views import CampaignViewSet, TagViewSet

#build a router and creates routes for campaigns and tags
router = routers.DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'tags', TagViewSet)

urlpatterns =[
    path('', include(router.urls)),
]