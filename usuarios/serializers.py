from django.contrib.auth.models import User
from rest_framework import serializers


class RegistroSerializer(serializers.ModelSerializer):
    """
    Serializer encargado de validar y registrar nuevos usuarios.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # create_user() permite que Django almacene la contraseña
        # utilizando su sistema de seguridad y no como texto plano.
        usuario = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

        return usuario