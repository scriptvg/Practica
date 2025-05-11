from rest_framework import serializers
from datetime import date
from .models import Cita

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
