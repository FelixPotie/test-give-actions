from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist

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
    

    @action(detail=True, methods=['put'])
    def addTag(self, request, pk=None):
        query = request.GET.get('query')
        campagne = self.get_object()
        try:
            tag = Tag.objects.get(pk=query)
            if Campagne.objects.filter(tags__id=query).filter(id=campagne.id).exists():
                return Response({'message': 'no change, tag '+str(tag)+' is already linked to the campaign '+str(campagne)})
            else:
                campagne.tags.add(tag)
                serializer = CampagneSerializer(campagne)
                return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'message': 'tag n°'+query+' does not exists'}, status=404)
        

    @action(detail=True, methods=['put'])
    def deleteTag(self, request, pk=None):
        query = request.GET.get('query')
        campagne = self.get_object()
        try:
            tag = Tag.objects.get(pk=query)
            if Campagne.objects.filter(tags__id=query).filter(id=campagne.id).exists():
                campagne.tags.remove(tag)
                serializer = CampagneSerializer(campagne)
                return Response(serializer.data)
            else:
                return Response({'message': 'tag '+str(tag)+' is not linked to the campaign '+str(campagne)}, status=404)
        except ObjectDoesNotExist:
            return Response({'message': 'tag n°'+query+' does not exists'}, status=404)
                


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer