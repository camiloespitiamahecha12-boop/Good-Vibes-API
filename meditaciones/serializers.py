from rest_framework import serializers

from .models import Meditacion


class MeditacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meditacion
        fields = [
            'id',
            'titulo',
            'descripcion',
            'tipo',
            'url',
            'duracion',
            'activa',
        ]
        read_only_fields = [
            'id',
        ]