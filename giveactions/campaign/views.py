from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist

from .serializers import TagSerializer, CampaignSerializer
from .models import Tag, Campaign

#views file, where API routes actions are implemented

#routes for Campaign: $id = the id of the campaign
#GET    /campaigns/                             get the list of all the campaigns
#GET    /campaigns/$id/                         get the campaigns informations for the one with the id id
#GET    /campaigns/byTag/?tag=$tagId            get the list of the campaigns which contains the tag with the id tagId
#POST   /campaigns/                             create a campaigns, without tags, the body must be a json file with the attribute found in the Campaign Model
#PUT    /campaigns/$id/                         modify the campaigns informations excepts of the tags
#PUT    /campaigns/$id/addTag/?tag=$tagId       modify by adding the tag with the tagId to the campaign with id
#PUT    /campaigns/$id/deleteTag/?tag=$tagId    modify by deleting the tag with the tagId to the campaign with id
#DELETE /campaigns/$id/                         delete the campaign with the id id
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
                

#routes for Tag: $id = the id of the tag
#GET    /tags/          get the list of all the tags
#GET    /tags/$id/      get the tags informations for the one with the id id
#POST   /tags/          create a tag, the body must be a json file with the attribute found in the Tag Model
#PUT    /tags/$id/      modify the tag informations with the id id
#DELETE /tags/$id/      delete the tag with the id id
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer