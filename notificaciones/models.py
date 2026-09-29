from django.db import models


class Notificacion(models.Model):

    TIPOS = [
        ('cita', 'Cita'),
        ('meditacion', 'Meditación'),
        ('recordatorio', 'Recordatorio'),
        ('general', 'General'),
    ]

    usuario = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150)
    mensaje = models.TextField()
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.titulo}'