from django.db import models

""" Modelo Paciente """
class Paciente(models.Model):
    nombre =                models.CharField(max_length=100)    # nombre del paciente
    edad =                  models.PositiveIntegerField()       # edad del paciente
# ============================================================== #
    # sexo del paciente (Masculino, Femenino)
    sexo =                  models.CharField(
        max_length=10, choices=[
            ('M', 'Masculino'),
            ('F', 'Femenino')]) 
# ============================================================== #
    correo =                models.EmailField(unique=True)                          # correo del paciente
    telefono =              models.CharField(max_length=20, blank=True, null=True)  # telefono del paciente
    direccion =             models.CharField(max_length=200, blank=True)            # direccion del paciente
    fecha_registro =        models.DateTimeField(auto_now_add=True)                 # fecha de registro del paciente
    numero_seguro_social =  models.CharField(max_length=20, unique=True)            # numero de seguro social
# ============================================================== #
    # tipo de sangre del paciente
    tipo_sangre =           models.CharField(
        max_length=3, choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ]) 
# ============================================================== #
    # retorna el nombre y la edad del paciente
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
