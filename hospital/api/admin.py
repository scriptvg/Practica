from django.contrib import admin
from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita

# ===================== PACIENTES =====================
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'sexo', 'correo', 'numero_seguro_social', 'tipo_sangre', 'fecha_registro')
    search_fields = ('nombre', 'correo', 'numero_seguro_social')
    list_filter = ('sexo', 'tipo_sangre')


# ===================== DOCTORES =====================
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anios_experiencia', 'correo', 'numero_licencia', 'activo')
    search_fields = ('nombre', 'correo', 'numero_licencia')
    list_filter = ('activo',)


# ===================== ESPECIALIDADES =====================
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area')
    search_fields = ('nombre',)
    list_filter = ('area',)


# ===================== DOCTOR - ESPECIALIDAD =====================
@admin.register(DoctorEspecialidad)
class DoctorEspecialidadAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'especialidad', 'nivel', 'fecha_certificacion')
    list_filter = ('nivel', 'fecha_certificacion')
    search_fields = ('doctor__nombre', 'especialidad__nombre')


# ===================== CITAS =====================
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('paciente__nombre', 'doctor__nombre', 'motivo')
