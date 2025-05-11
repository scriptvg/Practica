from rest_framework import serializers
from django.contrib.auth.models import User

# ===================== REGISTRO ===================== #
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# ===================== LOGIN ===================== #
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# ===================== PERFIL Y USUARIO ===================== #
class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'date_joined', 'last_login'
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'date_joined', 'last_login'
        ]
        read_only_fields = fields
