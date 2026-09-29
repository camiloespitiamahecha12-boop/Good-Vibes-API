from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cita
from .serializers import CitaSerializer


class CitaListCreateView(APIView):
    """
    Vista para consultar todas las citas
    y crear nuevas citas.
    """

    def get(self, request):
        citas = Cita.objects.all()
        serializer = CitaSerializer(citas, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = CitaSerializer(data=request.data)

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


class CitaDetailView(APIView):
    """
    Vista para consultar, actualizar y eliminar
    una cita específica.
    """

    def get_object(self, pk):
        try:
            return Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return None

    def get(self, request, pk):
        cita = self.get_object(pk)

        if cita is None:
            return Response(
                {
                    'mensaje': 'Cita no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CitaSerializer(cita)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        cita = self.get_object(pk)

        if cita is None:
            return Response(
                {
                    'mensaje': 'Cita no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CitaSerializer(
            cita,
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
        cita = self.get_object(pk)

        if cita is None:
            return Response(
                {
                    'mensaje': 'Cita no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        cita.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
)