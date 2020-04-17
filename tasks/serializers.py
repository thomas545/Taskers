from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import *
from .utils import ImageFieldName
from collections import OrderedDict


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    image = ImageFieldName(required=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("instance -> ", type(instance))
        print("validated_data -> ", validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def save(self, **kwargs):
        print("Send mail -> ")
        return super(CategorySerializer, self).save(**kwargs)


class CategoryFetchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    image = ImageFieldName(required=False)
