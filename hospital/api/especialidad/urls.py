from django.urls import path
from .views import EspecialidadListCreateView, EspecialidadDetailView

urlpatterns = [
    path('', EspecialidadListCreateView.as_view(), name='especialidad-list-create'),
    path('<int:pk>/', EspecialidadDetailView.as_view(), name='especialidad-detail'),
]
