from django.urls import path, include

urlpatterns = [
    path('pacientes/', include('api.paciente.urls')),
    path('doctores/', include('api.doctor.urls')),
    path('especialidades/', include('api.especialidad.urls')),
    path('doctor-especialidades/', include('api.doctor_especialidad.urls')),
    path('citas/', include('api.cita.urls')),
    path('auth/', include('api.authuser.urls')),
]
