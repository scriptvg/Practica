from rest_framework import serializers
from .models import DoctorEspecialidad

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
