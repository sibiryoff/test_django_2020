from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.images.viewsets import ImageViewSet

v1_router = DefaultRouter()

v1_router.register(r'images', ImageViewSet, basename='images')

urlpatterns = [
    path('', include(v1_router.urls)),
]
