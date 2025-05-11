from django.db import models

""" Modelo Especialidad """
class Especialidad(models.Model):
    nombre =        models.CharField(max_length=100, unique=True)   # nombre de la especialidad
    descripcion =   models.TextField(blank=True)                    # descripción de la especialidad
# ============================================================== #
    # área de la especialidad
    area = models.CharField(max_length=50, choices=[
        ('Medicina General', 'Medicina General'),
        ('Cirugía', 'Cirugía'),
        ('Pediatría', 'Pediatría'),
        ('Cardiología', 'Cardiología'),
        ('Dermatología', 'Dermatología'),
        ('Neurología', 'Neurología'),
    ])  
# ============================================================== #
    # retorna el nombre y la especialidad
    def __str__(self):
        return f"{self.nombre} - {self.area}"
