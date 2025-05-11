from django.urls import path
from .views import DoctorEspecialidadListCreateView, DoctorEspecialidadDetailView

urlpatterns = [
    path('', DoctorEspecialidadListCreateView.as_view(), name='doctor-especialidad-list-create'),
    path('<int:pk>/', DoctorEspecialidadDetailView.as_view(), name='doctor-especialidad-detail'),
]
