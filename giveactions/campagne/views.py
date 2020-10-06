from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TagSerializer, CampagneSerializer
from .models import Tag, Campagne

class CampagneViewSet(viewsets.ModelViewSet):
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer

    @action(detail=False)
    def byTag(self, request):
        query = request.GET.get('query')
        campagnes = Campagne.objects.filter(tags__id=query)
        serializer = CampagneSerializer(campagnes, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer