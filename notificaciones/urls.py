from django.urls import path

from .views import NotificacionDetailView, NotificacionListCreateView


urlpatterns = [
    path(
        'notificaciones/',
        NotificacionListCreateView.as_view(),
        name='lista-notificaciones'
    ),
    path(
        'notificaciones/<int:pk>/',
        NotificacionDetailView.as_view(),
        name='detalle-notificacion'
    ),
]