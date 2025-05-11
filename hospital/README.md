# 🏥 API de Gestión Hospitalaria – Quiz #5

Este proyecto es una API REST creada con Django y Django REST Framework para gestionar pacientes, doctores, especialidades médicas y citas.

## ✅ Funcionalidades

- CRUD para:
  - Pacientes
  - Doctores
  - Especialidades
  - Relación doctores-especialidades
  - Citas médicas
- Validaciones con `raise` en serializers
- Rutas limpias gracias a ViewSets + Router
- Página de bienvenida en `/`
- Pruebas compatibles con Postman/ThunderBolt

## 🚀 Instalación

1. Clona el proyecto y entra a la carpeta:
   ```bash
   git clone https://github.com/tu-usuario/quiz-hospital-api.git
   cd quiz-hospital-api
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu base de datos en `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'hospital',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Aplica las migraciones y corre el servidor:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## 📂 Endpoints

Todos los recursos están bajo `/api/`:

| Recurso              | Endpoint                 |
|----------------------|--------------------------|
| Pacientes            | `/api/pacientes/`        |
| Doctores             | `/api/doctores/`         |
| Especialidades       | `/api/especialidades/`   |
| DoctorEspecialidad   | `/api/doctor-especialidades/` |
| Citas                | `/api/citas/`            |

## 🧪 Pruebas recomendadas

En Postman/Insomnia:

- `GET /api/pacientes/`
- `POST /api/pacientes/` (creación)
- `PUT /api/pacientes/<id>/`
- `DELETE /api/pacientes/<id>/`

Repetir para los demás modelos.

## 🛠 Tecnologías

- Django
- Django REST Framework
- MySQL / MariaDB
- Postman/ThunderBolt
