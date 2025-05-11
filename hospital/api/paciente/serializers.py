from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    def validate_edad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La edad debe ser mayor que cero.")
        return value
        