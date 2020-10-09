from rest_framework import serializers

from .models import Campaign, Tag

#this file serialize and deserialize the objects into json 

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',)

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Campaign
        fields = ('id','title', 'description', 'image', 'tags')
