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
from io import BytesIO
import zipfile
import hashlib

class PredictionHTMLView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Prediction.objects.all()
        serializer_class = PredictionSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):

        html_data = request.data.get('html_data','')
        with open('index.html', 'wb') as f:
            f.write(html_data.encode('utf-8'))
        with open("netlify.toml", "w") as f:
            f.write("[[redirects]]\n  from = \"/*\"\n  to = \"/index.html\"\n  status = 200\n")

        with zipfile.ZipFile("website.zip", mode="w") as zf:
            zf.write('index.html')
            zf.write("netlify.toml")
        
        site_name = request.data.get('site_name', 'My Site')
        access_token = "mcMX6BXdqcQIvjgChC2f9NnZCWPqEa7h6dJjwlbvhVg"
        api_endpoint = "https://api.netlify.com/api/v1/sites"
        with open('website.zip', 'rb') as f:
            response = requests.post(
                api_endpoint,
                headers={
                    "Content-Type": "application/zip",
                    "Authorization": f"Bearer {access_token}"
                },
                data=f,
                params={
                    "name": site_name,
                }

            )
            deployed_url = f'https://{site_name}.netlify.app'
        return Response({'deployed_url': deployed_url})
