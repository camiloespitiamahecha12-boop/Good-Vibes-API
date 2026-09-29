from django.db import models


class Meditacion(models.Model):

    TIPOS = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.CharField(
        max_length=10,
        choices=TIPOS
    )
    url = models.URLField()
    duracion = models.PositiveIntegerField(
        help_text='Duración en minutos'
    )
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo