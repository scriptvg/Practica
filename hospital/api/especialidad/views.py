from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Especialidad
from .serializers import EspecialidadSerializer
from api.authuser.permissions import IsAuthenticatedUserRole

class EspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]

class EspecialidadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [JWTAuthentication]
