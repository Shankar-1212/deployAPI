from rest_framework import viewsets
from ..models import Prediction
from .serializers import PredictionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
import numpy as np
import os
import requests

class PredictionView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Prediction.objects.all()
        serializer_class = PredictionSerializer(
            queryset, many=True, context={'request': request})
        return Response(seriali1zer_class.data)
    def post(self, request, *args, **kwargs):
        parser_classes = (MultiPartParser, FormParser)
        if request.content_type == 'text/plain':
            text_data = request.body.decode('utf-8')
            return HttpResponse('<h1>Hello, {}</h1>'.format(text_data))
