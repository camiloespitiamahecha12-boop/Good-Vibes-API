from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notificacion
from .serializers import NotificacionSerializer


class NotificacionListCreateView(APIView):
    """
    Vista para consultar todas las notificaciones
    y crear nuevas notificaciones.
    """

    def get(self, request):
        notificaciones = Notificacion.objects.all()
        serializer = NotificacionSerializer(
            notificaciones,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = NotificacionSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class NotificacionDetailView(APIView):
    """
    Vista para consultar, actualizar y eliminar
    una notificación específica.
    """

    def get_object(self, pk):
        try:
            return Notificacion.objects.get(pk=pk)
        except Notificacion.DoesNotExist:
            return None

    def get(self, request, pk):
        notificacion = self.get_object(pk)

        if notificacion is None:
            return Response(
                {
                    'mensaje': 'Notificación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NotificacionSerializer(notificacion)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        notificacion = self.get_object(pk)

        if notificacion is None:
            return Response(
                {
                    'mensaje': 'Notificación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NotificacionSerializer(
            notificacion,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        notificacion = self.get_object(pk)

        if notificacion is None:
            return Response(
                {
                    'mensaje': 'Notificación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        notificacion.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )