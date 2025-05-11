from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Doctor
from .serializers import DoctorSerializer
from api.authuser.permissions import IsAuthenticatedUserRole

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]
