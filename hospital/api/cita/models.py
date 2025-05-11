from django.db import models
from api.paciente.models import Paciente
from api.doctor.models import Doctor

""" Modelo Cita """ 
class Cita(models.Model):
    paciente =  models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas') # paciente que tiene la cita
    doctor =    models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')   # doctor que atiende la cita
    fecha =     models.DateField()   # fecha de la cita
    hora =      models.TimeField()   # hora de la cita
    motivo =    models.TextField()   # motivo de la cita
# ============================================================== #
    # estado de la cita
    estado = models.CharField(max_length=20, choices=[
        ('Programada', 'Programada'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
        ('No Asistió', 'No Asistió'),
    ], default='Programada')
# ============================================================== #
    notas_medico =      models.TextField(blank=True, null=True) # notas del médico
    notas_paciente =    models.TextField(blank=True, null=True) # notas del paciente
# ============================================================== #
    def __str__(self):
        return f"Cita {self.fecha} {self.hora} con Dr. {self.doctor.nombre}"
