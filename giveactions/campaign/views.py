from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist

from .serializers import TagSerializer, CampaignSerializer
from .models import Tag, Campaign

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    @action(detail=False)
    def byTag(self, request):
        tag = request.GET.get('tag')
        campaigns = Campaign.objects.filter(tags__id=tag)
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['put'])
    def addTag(self, request, pk=None):
        tagId = request.GET.get('tag')
        campaign = self.get_object()
        try:
            tag = Tag.objects.get(pk=tagId)
            if Campaign.objects.filter(tags__id=tagId).filter(id=campaign.id).exists():
                return Response({'message': 'no change, tag '+str(tag)+' is already linked to the campaign '+str(campaign)})
            else:
                campaign.tags.add(tag)
                serializer = CampaignSerializer(campaign)
                return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'message': 'tag n°'+str(tagId)+' does not exists'}, status=404)
        

    @action(detail=True, methods=['put'])
    def deleteTag(self, request, pk=None):
        tagId = request.GET.get('tag')
        campaign = self.get_object()
        try:
            tag = Tag.objects.get(pk=tagId)
            if Campaign.objects.filter(tags__id=tagId).filter(id=campaign.id).exists():
                campaign.tags.remove(tag)
                serializer = CampaignSerializer(campaign)
                return Response(serializer.data)
            else:
                return Response({'message': 'tag '+str(tag)+' is not linked to the campaign '+str(campaign)}, status=404)
        except ObjectDoesNotExist:
            return Response({'message': 'tag n°'+str(tagId)+' does not exists'}, status=404)
                


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer