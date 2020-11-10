from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.images.models import Image
from apps.images.serializers import ImageSerializer


class ImageViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
