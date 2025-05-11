from rest_framework import serializers
from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita
from django.contrib.auth.models import User
from datetime import date

# ===================== AUTH ===================== #
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
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'date_joined', 'last_login'
        ]
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined', 'last_login']
        read_only_fields = ['id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'date_joined', 'last_login']

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

# ===================== PACIENTE ===================== #
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    def validate_edad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La edad debe ser mayor que cero.")
        return value

# ===================== DOCTOR ===================== #
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_anios_experiencia(self, value):
        if value < 0:
            raise serializers.ValidationError("Los años de experiencia no pueden ser negativos.")
        return value

# ===================== ESPECIALIDAD ===================== #
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

# ===================== DOCTOR-ESPECIALIDAD ===================== #
class DoctorEspecialidadSerializer(serializers.ModelSerializer):
    doctor_nombre = serializers.CharField(source='doctor.nombre', read_only=True)
    especialidad_nombre = serializers.CharField(source='especialidad.nombre', read_only=True)

    class Meta:
        model = DoctorEspecialidad
        fields = [
            'id', 'doctor', 'especialidad', 'fecha_certificacion', 'nivel',
            'doctor_nombre', 'especialidad_nombre'
        ]

    def validate_nivel(self, value):
        if value not in ['Junior', 'Senior', 'Consultor']:
            raise serializers.ValidationError("Nivel inválido. Use Junior, Senior o Consultor.")
        return value

# ===================== CITA ===================== #
class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(source='paciente.nombre', read_only=True)
    doctor_nombre = serializers.CharField(source='doctor.nombre', read_only=True)

    class Meta:
        model = Cita
        fields = [
            'id', 'paciente', 'doctor', 'fecha', 'hora',
            'motivo', 'estado', 'notas_medico', 'notas_paciente',
            'paciente_nombre', 'doctor_nombre'
        ]

    def validate_fecha(self, value):
        if value < date.today():
            raise serializers.ValidationError("La fecha de la cita no puede estar en el pasado.")
        return value
