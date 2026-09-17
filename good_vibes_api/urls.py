from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Conecta las rutas de la aplicación de usuarios
    # con las rutas principales del proyecto.
    path('api/', include('usuarios.urls')),
]