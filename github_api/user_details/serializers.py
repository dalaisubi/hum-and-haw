from rest_framework import serializers
from .models import Owner, ReposDetail

class ReposDetailSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return ReposDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance = validated_data.get('title', instance.title)
        instance.save()
        return instance