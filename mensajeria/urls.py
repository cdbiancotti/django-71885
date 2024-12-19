from django.urls import path
from mensajeria import views

app_name = 'mensajeria'

urlpatterns = [
    path('enviar_mensaje/', views.EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
    path('listado_mensajes/', views.listar_mensajes, name='listar_mensajes'),
]
