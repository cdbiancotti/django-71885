from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', views.login, name='iniciar_sesion'),
    path('cerrar-sesion/', views.CerrarSesion.as_view(), name='cerrar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/edicion/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
]
