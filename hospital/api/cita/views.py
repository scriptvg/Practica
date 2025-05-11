from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Cita
from .serializers import CitaSerializer
from api.authuser.permissions import IsAuthenticatedUserRole

class CitaListCreateView(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]

class CitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]
