from django.db import models


class Cita(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    cliente = models.CharField(max_length=100)
    profesional = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )
    motivo = models.TextField()

    def __str__(self):
        return f'{self.cliente} - {self.fecha} {self.hora}'