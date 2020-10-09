from rest_framework import serializers

from .models import Campagne, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','nom',)

class CampagneSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Campagne
        fields = ('id','titre', 'description', 'image', 'tags')
