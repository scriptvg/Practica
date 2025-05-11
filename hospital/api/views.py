from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.models import Group, User
from django.shortcuts import render

from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita
from .serializers import (
    PacienteSerializer,
    DoctorSerializer,
    EspecialidadSerializer,
    DoctorEspecialidadSerializer,
    CitaSerializer,
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer, UserProfileSerializer
)

# ===================== PERMISOS PERSONALIZADOS ===================== #
class IsAdminUserGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()

class IsAuthenticatedUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(
            Q(name='admin') | Q(name='doctor') | Q(name='paciente')
        ).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.groups.filter(Q(name='admin') | Q(name='doctor')).exists()
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.groups.filter(Q(name='admin') | Q(name='doctor') | Q(name='paciente')).exists()
        return False

# ===================== REGISTRO DE USUARIO ===================== #
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Asegúrate de que el grupo 'paciente' exista
            group, created = Group.objects.get_or_create(name='paciente')
            if created:
                print("Grupo 'paciente' creado.")
            else:
                print("Grupo 'paciente' ya existe.")
            user.groups.add(group)
            print(f"Usuario {user.username} agregado al grupo 'paciente'.")
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===================== LOGIN DE USUARIO ===================== #

class UserLoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# ===================== LOGOUT DE USUARIO ===================== #
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# ===================== PERFIL DEL USUARIO ===================== #
class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# ===================== HOME ===================== #
class HomeAPIView(APIView):
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        return Response({
            "mensaje": "Bienvenido a la API del Hospital 🏥",
            "endpoints": [
                "http://127.0.0.1:8000/api/pacientes/",
                "http://127.0.0.1:8000/api/doctores/",
                "http://127.0.0.1:8000/api/especialidades/",
                "http://127.0.0.1:8000/api/doctor-especialidades/",
                "http://127.0.0.1:8000/api/citas/",
                "http://127.0.0.1:8000/api/auth/register/",
                "http://127.0.0.1:8000/api/auth/login/",
                "http://127.0.0.1:8000/api/auth/profile/",
            ]
        })

# ===================== CRUD PACIENTE ===================== #
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

# ===================== CRUD DOCTOR ===================== #
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

# ===================== CRUD ESPECIALIDAD ===================== #
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

# ===================== CRUD DOCTOR-ESPECIALIDAD ===================== #
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

# ===================== CRUD CITAS ===================== #
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

# ===================== VISTA HTML LOGIN (Opcional) ===================== #
def login(request):
    return render(request, 'login.html')