from rest_framework import serializers

from .models import Campagne, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('nom',)

class CampagneSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Campagne
        fields = ('titre', 'description', 'image', 'tags')
