from django.urls import path
from .views import CitaListCreateView, CitaDetailView

urlpatterns = [
    path('', CitaListCreateView.as_view(), name='cita-list-create'),
    path('<int:pk>/', CitaDetailView.as_view(), name='cita-detail'),
]
