from django.urls import path

from .views import ObservacionDetailView, ObservacionListCreateView


urlpatterns = [
    path(
        'observaciones/',
        ObservacionListCreateView.as_view(),
        name='lista-observaciones'
    ),
    path(
        'observaciones/<int:pk>/',
        ObservacionDetailView.as_view(),
        name='detalle-observacion'
    ),
]