from django.db import models

# ============ Modelos ============ #


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
# ============================================================== #

""" Modelo Doctor """
class Doctor(models.Model):
    nombre =            models.CharField(max_length=100)                        # nombre del doctor
    anios_experiencia = models.PositiveIntegerField()                           # años de experiencia del doctor
    correo =            models.EmailField(unique=True)                          # correo del doctor
    telefono =          models.CharField(max_length=20, blank=True, null=True)  # telefono del doctor
    numero_licencia =   models.CharField(max_length=50, unique=True)            # numero de licencia del doctor
    activo =            models.BooleanField(default=True)                       # si el doctor esta activo o no
    horario =           models.CharField(max_length=100, blank=True)            # horario del doctor
# ============================================================== #
    # retorna el nombre y la edad del doctor
    def __str__(self):
        return f"{self.nombre} - {self.area}"
# ============================================================== #
    
""" Modelo Especialidad """
class Especialidad(models.Model):
    nombre =        models.CharField(max_length=100, unique=True)   # nombre de la especialidad
    descripcion =   models.TextField(blank=True)                    # descripcion de la especialidad
# ============================================================== #
    # area de la especialidad
    area = models.CharField(max_length=50, choices=[
        ('Medicina General', 'Medicina General'),
        ('Cirugía', 'Cirugía'),
        ('Pediatría', 'Pediatría'),
        ('Cardiología', 'Cardiología'),
        ('Dermatología', 'Dermatología'),
        ('Neurología', 'Neurología'),
    ])  
# ============================================================== #
    # retorna el nombre y la especialidad del doctor
    def __str__(self):
        return f"{self.nombre} - {self.area}"
# ============================================================== #

""" Modelo Doctor_Especialidad """    
class DoctorEspecialidad(models.Model):
    doctor =                models.ForeignKey(Doctor, on_delete=models.CASCADE)         # doctor que tiene la especialidad
    especialidad =          models.ForeignKey(Especialidad, on_delete=models.CASCADE)   # especialidad del doctor
    fecha_certificacion =   models.DateField(blank=True, null=True)                     # fecha de certificacion del doctor
# ============================================================== #
    # nivel del doctor
    nivel = models.CharField(max_length=20, choices=[
        ('Junior', 'Junior'), ('Senior', 'Senior'), ('Consultor', 'Consultor')
    ])
# ============================================================== #
    # clave unica para la combinacion de doctor y especialidad
    class Meta:
        unique_together = ('doctor', 'especialidad')
# ============================================================== #
    # retorna nombre del doctor, especialidad del doctor y su nivel
    def __str__(self):
        return f"{self.doctor.nombre} - {self.especialidad.nombre} ({self.nivel})"
# ============================================================== #

""" Modelo Cita """ 
class Cita(models.Model):
    paciente =  models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas') # paciente que tiene la cita
    doctor =    models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')   # doctor que atiende la cita
    fecha =     models.DateField() # fecha de la cita
    hora =      models.TimeField() # hora de la cita
    motivo =    models.TextField() # motivo de la cita
# ============================================================== #
    # estado de la cita
    estado = models.CharField(max_length=20, choices=[
        ('Programada', 'Programada'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
        ('No Asistió', 'No Asistió'),
    ], default='Programada')
# ============================================================== #
    notas_medico =      models.TextField(blank=True, null=True) # notas del medico
    notas_paciente =    models.TextField(blank=True, null=True) # notas del paciente
# ============================================================== #
    # retorna el doctor, la hora y fecha de la cita
    def __str__(self):
        return f"Cita {self.fecha} {self.hora} con Dr. {self.doctor.nombre}"
# ============================================================== #
