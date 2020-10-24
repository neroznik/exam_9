from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed, request
from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Picture


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class AddFavSet(APIView):
    def post(self, request, pk=None):
        picture = get_object_or_404(Picture, pk=pk)
        created = Picture.objects.get_or_create(picture=picture, user=request.user)
        if created:
            picture.save()
            return Response({'pk': pk})
        else:
            return Response(status=403)

class RemoveFavSet(APIView):
    def delete(self, request, pk=None):
        picture = get_object_or_404(Picture, pk=pk)
        picture.delete()
        return Response({'pk': pk})
