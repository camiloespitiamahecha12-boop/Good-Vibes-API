from django.urls import path

from .views import CitaDetailView, CitaListCreateView


urlpatterns = [
    path(
        'citas/',
        CitaListCreateView.as_view(),
        name='lista-citas'
    ),
    path(
        'citas/<int:pk>/',
        CitaDetailView.as_view(),
        name='detalle-cita'
    ),
]