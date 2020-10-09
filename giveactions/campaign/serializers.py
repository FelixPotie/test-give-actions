from rest_framework import serializers

from .models import Campaign, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','nom',)

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Campaign
        fields = ('id','titre', 'description', 'image', 'tags')
