from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_anios_experiencia(self, value):
        if value < 0:
            raise serializers.ValidationError("Los años de experiencia no pueden ser negativos.")
        return value

    def validate_edad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La edad debe ser mayor que cero.")
        return value