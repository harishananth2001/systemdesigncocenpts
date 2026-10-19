# A Django model instance might represent a patient:  1
patient.name = "Harish"
patient.age = 25
#  Django REST Framework can serialize the instance into JSON: 2
{
  "id": 1,
  "name": "Harish",
  "age": 25
}

# Django REST Framework example 4
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "age"]