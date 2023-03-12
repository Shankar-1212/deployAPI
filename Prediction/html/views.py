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

class PredictionHTMLView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Prediction.objects.all()
        serializer_class = PredictionSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer_class.data)
    def post(self, request, *args, **kwargs):
        if request.content_type == 'application/zip':
            zip_file = BytesIO(request.body)
            api_endpoint = "https://api.netlify.com/api/v1/sites"
            access_token = ""
            headers = {"Authorization": f"Bearer {access_token}"}
            files = {"file": ("website.zip", zip_file, "application/zip")}
            response = requests.post(api_endpoint, headers=headers, data=files)
            site_id = response.json().get("site_id")
            deploy_endpoint = f"{api_endpoint}/{site_id}/deploys"
            response = requests.post(deploy_endpoint, headers=headers)
            return Response(response.json())
        else:
            return Response({"error": "Invalid content type."}, status=status.HTTP_400_BAD_REQUEST)
