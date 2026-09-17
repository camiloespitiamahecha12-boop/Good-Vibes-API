# Good Vibes API

## Descripción

Good Vibes API es un servicio web desarrollado con Django y Django REST Framework para gestionar el registro y la autenticación de usuarios.

Este servicio forma parte del proyecto Good Vibes, una aplicación orientada al bienestar emocional de los usuarios.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub

## Funcionalidades

### Registro de usuarios

Permite crear un nuevo usuario mediante una solicitud POST.

**Endpoint:**

`POST /api/registro/`

**Datos requeridos:**

```json
{
    "username": "camilo",
    "email": "camilo@gmail.com",
    "password": "12345678"
}