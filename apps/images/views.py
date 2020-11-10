from django.core.exceptions import ObjectDoesNotExist
from django.http import (JsonResponse, QueryDict, HttpResponseBadRequest,
                         HttpResponse)
from django.shortcuts import render
from django.views import View

from apps.images.forms import ImageForm
from apps.images.models import Image


class ImageUploadView(View):

    def get(self, request):
        images = Image.objects.all().order_by("-uploaded_at")
        return render(request, 'index.html', {'images': images})

    def post(self, request):
        form = ImageForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            image = form.save()
            data = {
                'is_valid': True,
                'name': image.image.name,
                'url': image.image.url,
                'tmb_url': image.image['thumbnail'].url,
                'size': image.image.size,
                'width': image.image.width,
                'height': image.image.height,
                'pk': image.pk
            }
        else:
            data = {'is_valid': False}

        return JsonResponse(data)

    def delete(self, request):
        data = QueryDict(request.body)
        if data and data.get('pk', None):
            try:
                img = Image.objects.get(pk=data['pk'])
                img.delete()
            except ObjectDoesNotExist:
                return HttpResponseBadRequest(f"No image with pk={data['pk']}")
            return HttpResponse("ok")
        else:
            return HttpResponseBadRequest()
