from rest_framework.serializers import ImageField


class ImageFieldName(ImageField):
    def to_representation(self, value):
        return value.name
