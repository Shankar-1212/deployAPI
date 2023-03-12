from django.urls import path
import Prediction.views as views
# from rest_framework import routers
from .views import PredictionHTMLView

# router = routers.DefaultRouter()
# router.register(r'', views.PredictionView)
urlpatterns=[
    path('', PredictionHTMLView.as_view(), name='prediction1'),
]


