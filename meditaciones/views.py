from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Meditacion
from .serializers import MeditacionSerializer


class MeditacionListCreateView(APIView):
    """
    Vista para consultar todas las meditaciones
    y crear nuevas meditaciones.
    """

    def get(self, request):
        meditaciones = Meditacion.objects.all()
        serializer = MeditacionSerializer(
            meditaciones,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = MeditacionSerializer(
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


class MeditacionDetailView(APIView):
    """
    Vista para consultar, actualizar y eliminar
    una meditación específica.
    """

    def get_object(self, pk):
        try:
            return Meditacion.objects.get(pk=pk)
        except Meditacion.DoesNotExist:
            return None

    def get(self, request, pk):
        meditacion = self.get_object(pk)

        if meditacion is None:
            return Response(
                {
                    'mensaje': 'Meditación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MeditacionSerializer(meditacion)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        meditacion = self.get_object(pk)

        if meditacion is None:
            return Response(
                {
                    'mensaje': 'Meditación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MeditacionSerializer(
            meditacion,
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
        meditacion = self.get_object(pk)

        if meditacion is None:
            return Response(
                {
                    'mensaje': 'Meditación no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        meditacion.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )