from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Observacion
from .serializers import ObservacionSerializer


class ObservacionListCreateView(APIView):
    """
    Vista para consultar todas las observaciones
    y crear nuevas observaciones.
    """

    def get(self, request):
        observaciones = Observacion.objects.all()
        serializer = ObservacionSerializer(
            observaciones,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = ObservacionSerializer(
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


class ObservacionDetailView(APIView):
    """
    Vista para consultar, actualizar y eliminar
    una observación específica.
    """

    def get_object(self, pk):
        try:
            return Observacion.objects.get(pk=pk)
        except Observacion.DoesNotExist:
            return None

    def get(self, request, pk):
        observacion = self.get_object(pk)

        if observacion is None:
            return Response(
                {
                    'mensaje': 'Observación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ObservacionSerializer(observacion)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        observacion = self.get_object(pk)

        if observacion is None:
            return Response(
                {
                    'mensaje': 'Observación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ObservacionSerializer(
            observacion,
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
        observacion = self.get_object(pk)

        if observacion is None:
            return Response(
                {
                    'mensaje': 'Observación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        observacion.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )