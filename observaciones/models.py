from django.db import models

from citas.models import Cita


class Observacion(models.Model):

    cita = models.ForeignKey(
        Cita,
        on_delete=models.CASCADE,
        related_name='observaciones'
    )

    profesional = models.CharField(max_length=100)
    observacion = models.TextField()
    recomendacion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Observación - {self.profesional} - Cita {self.cita.id}'