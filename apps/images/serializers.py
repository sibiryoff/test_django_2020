import os

from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from apps.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    tmb_url = serializers.SerializerMethodField()
    name = serializers.CharField(source='image.name')
    width = serializers.IntegerField(source='image.width')
    height = serializers.IntegerField(source='image.height')
    size = serializers.IntegerField(source='image.size')
    ext = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["pk", "url", "tmb_url",
                  "name", "width", "height", "size", "ext", "uploaded_at"]

    def get_url(self, obj):
        url = obj.image.url
        request = self.context.get('request')
        return request.build_absolute_uri(url)

    def get_tmb_url(self, obj):
        url = get_thumbnailer(obj.image)['thumbnail'].url
        request = self.context.get('request')
        return request.build_absolute_uri(url)

    def get_ext(self, obj):
        return os.path.splitext(obj.image.name)[1].split('.')[-1]
