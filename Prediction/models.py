from django.db import models

# Create your models here.
class Prediction(models.Model):
    text=models.TextField()
    prediction=models.TextField()
class PredictionHTML(models.Model):
    html=models.FileField(upload_to='html_files', blank=True, null=True)