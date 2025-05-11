from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.authuser.permissions import IsAuthenticatedUserRole
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class HomeAPIView(APIView):
    permission_classes = [IsAuthenticatedUserRole]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        return Response({
            "mensaje": "Bienvenido a la API del Hospital 🏥",
            "endpoints": [
                "/api/paciente/",
                "/api/doctor/",
                "/api/especialidad/",
                "/api/doctor-especialidad/",
                "/api/cita/",
                "/api/auth/register/",
                "/api/auth/login/",
                "/api/auth/profile/",
            ]
        })

def login(request):
    from django.shortcuts import render
    return render(request, 'login.html')
