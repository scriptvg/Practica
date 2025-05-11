from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import DoctorEspecialidad
from .serializers import DoctorEspecialidadSerializer
from api.authuser.permissions import IsAuthenticatedUserRole

class DoctorEspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]

class DoctorEspecialidadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]
