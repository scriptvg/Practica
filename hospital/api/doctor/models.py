from django.db import models

""" Modelo Doctor """
class Doctor(models.Model):
    nombre =            models.CharField(max_length=100)                        # nombre del doctor
    anios_experiencia = models.PositiveIntegerField()                           # años de experiencia del doctor
    correo =            models.EmailField(unique=True)                          # correo del doctor
    telefono =          models.CharField(max_length=20, blank=True, null=True)  # telefono del doctor
    numero_licencia =   models.CharField(max_length=50, unique=True)            # numero de licencia del doctor
    activo =            models.BooleanField(default=True)                       # si el doctor esta activo o no
    horario =           models.CharField(max_length=100, blank=True)            # horario del doctor

    def __str__(self):
        return f"{self.nombre}"
