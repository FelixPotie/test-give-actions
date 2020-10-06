from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import TagSerializer, CampagneSerializer
from .models import Tag, Campagne

class CampagneViewSet(viewsets.ModelViewSet):
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer