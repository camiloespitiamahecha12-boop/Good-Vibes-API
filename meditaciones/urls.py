from django.urls import path

from .views import MeditacionDetailView, MeditacionListCreateView


urlpatterns = [
    path(
        'meditaciones/',
        MeditacionListCreateView.as_view(),
        name='lista-meditaciones'
    ),
    path(
        'meditaciones/<int:pk>/',
        MeditacionDetailView.as_view(),
        name='detalle-meditacion'
    ),
]