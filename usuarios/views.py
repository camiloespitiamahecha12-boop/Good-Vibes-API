from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistroSerializer
from django.contrib.auth import authenticate


class RegistroView(APIView):
    """
    Vista encargada de recibir las solicitudes de registro
    y crear nuevos usuarios en el sistema.
    """

    def post(self, request):
        # El serializer recibe y valida los datos enviados
        # mediante la solicitud POST.
        serializer = RegistroSerializer(data=request.data)

        if serializer.is_valid():
            # Si los datos son válidos, se crea el usuario.
            serializer.save()

            return Response(
                {
                    'mensaje': 'Usuario registrado correctamente'
                },
                status=status.HTTP_201_CREATED
            )

        # Si los datos no cumplen las validaciones,
        # se devuelve la información correspondiente al error.
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    """
    Vista encargada de verificar las credenciales
    de un usuario que desea iniciar sesión.
    """

    def post(self, request):
        # Obtenemos el usuario y la contraseña enviados
        # en la solicitud.
        username = request.data.get('username')
        password = request.data.get('password')

        # Verificamos que ambos datos hayan sido enviados.
        if not username or not password:
            return Response(
                {
                    'mensaje': 'El usuario y la contraseña son obligatorios'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Django verifica si las credenciales son correctas.
        usuario = authenticate(
            username=username,
            password=password
        )

        if usuario is not None:
            # Si las credenciales son correctas,
            # se devuelve una respuesta exitosa.
            return Response(
                {
                    'mensaje': 'Autenticación satisfactoria'
                },
                status=status.HTTP_200_OK
            )

        # Si las credenciales no son correctas,
        # se informa el error de autenticación.
        return Response(
            {
                'mensaje': 'Error en la autenticación'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )