from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='auth-register'),
    path('login/', UserLoginView.as_view(), name='auth-login'),
    path('logout/', UserLogoutView.as_view(), name='auth-logout'),
    path('profile/', UserProfileView.as_view(), name='auth-profile'),
    path('token/', TokenObtainPairView.as_view())
]
