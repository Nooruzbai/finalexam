from datetime import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Advertisement


class ModerateStatus(APIView):

    def get(self, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        advertisement.status = 'published'
        advertisement.date_published = datetime.now()
        advertisement.save()
        return Response(data={'message': 'Successfully moderated'})


class CancelStatus(APIView):
    def get(self, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        advertisement.status = 'canceled'
        advertisement.save()
        return Response(data={'message': 'Successfully canceled'})