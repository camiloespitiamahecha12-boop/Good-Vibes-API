from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Conecta las rutas de la aplicación de usuarios
    # con las rutas principales del proyecto.
    path('api/', include('usuarios.urls')),
    # Rutas de citas.
    path('api/', include('citas.urls')),
    #ruta de observaciones
    path('api/', include('observaciones.urls')),
    #ruta de meditaciones
    path('api/', include('meditaciones.urls')),
    #ruta de notificaciones
    path('api/', include('notificaciones.urls')),
]