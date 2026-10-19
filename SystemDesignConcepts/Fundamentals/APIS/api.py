# Django code
# Create a patient model in models.py 

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

# Create a serializer in serializers.py:
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "age", "email"]

# Create a protected read-only API in views.py:
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Patient
from .serializers import PatientSerializer

class PatientListAPI(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAdminUser]

# In urls.py:
from django.urls import path
from .views import PatientListAPI

urlpatterns = [
    path("api/patients/", PatientListAPI.as_view()),
]

# This assumes Django REST Framework and 
# authentication are configured, the model is migrated, and 
# the application URL configuration includes this route.