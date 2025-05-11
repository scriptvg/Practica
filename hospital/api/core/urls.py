from django.urls import path
from .views import HomeAPIView, login

urlpatterns = [
    path('', HomeAPIView.as_view(), name='api-home'),
    path('login/', login, name='html-login'),  # opcional si usas HTML
]
