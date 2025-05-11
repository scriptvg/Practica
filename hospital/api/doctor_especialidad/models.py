from django.db import models
from api.doctor.models import Doctor
from api.especialidad.models import Especialidad

""" Modelo Doctor_Especialidad """    
class DoctorEspecialidad(models.Model):
    doctor =                models.ForeignKey(Doctor, on_delete=models.CASCADE)         # doctor que tiene la especialidad
    especialidad =          models.ForeignKey(Especialidad, on_delete=models.CASCADE)   # especialidad del doctor
    fecha_certificacion =   models.DateField(blank=True, null=True)                     # fecha de certificación del doctor
# ============================================================== #
    # nivel del doctor
    nivel = models.CharField(max_length=20, choices=[
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Consultor', 'Consultor')
    ])
# ============================================================== #
    class Meta:
        unique_together = ('doctor', 'especialidad')  # combinación única

    def __str__(self):
        return f"{self.doctor.nombre} - {self.especialidad.nombre} ({self.nivel})"
