from django.db import models
from django.db.models import DateTimeField, PositiveIntegerField
from easy_thumbnails.fields import ThumbnailerImageField


class Image(models.Model):
    image = ThumbnailerImageField(upload_to='images/')
    uploaded_at = DateTimeField(auto_now_add=True)
