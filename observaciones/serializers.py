from rest_framework import serializers

from .models import Observacion


class ObservacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observacion
        fields = [
            'id',
            'cita',
            'profesional',
            'observacion',
            'recomendacion',
            'fecha_registro',
        ]
        read_only_fields = [
            'id',
            'fecha_registro',
        ]