from django.urls import path

from .views import LoginView, RegistroView


urlpatterns = [
    # Endpoint utilizado para registrar nuevos usuarios.
    path('registro/', RegistroView.as_view(), name='registro'),

    # Endpoint utilizado para iniciar sesión.
    path('login/', LoginView.as_view(), name='login'),
]