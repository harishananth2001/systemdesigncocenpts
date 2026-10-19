# Django security code
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class PatientListAPI(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAdminUser]