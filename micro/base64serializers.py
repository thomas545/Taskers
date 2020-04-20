from django.db import models

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer 

from .base64fields import Base64FileMixinField, Base64ImageMixinField


class Base64ModelSerializerMixin(object):

    def __init__(self, *args, **kwargs):
        self.serializer_field_mapping.update({
            models.FileField: Base64FileMixinField,
            models.ImageField: Base64ImageMixinField,
        })
        super(Base64ModelSerializerMixin, self).__init__(*args, **kwargs)


class Base64ModelSerializer(Base64ModelSerializerMixin, ModelSerializer):
    pass


class Base64HyperlinkedModelSerializer(Base64ModelSerializerMixin, HyperlinkedModelSerializer):
    pass