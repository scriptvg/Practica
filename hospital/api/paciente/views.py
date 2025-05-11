from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Paciente
from .serializers import PacienteSerializer
from api.authuser.permissions import IsAuthenticatedUserRole

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]
