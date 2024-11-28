from inicio.views import bienvenida, fecha_y_hora, saludo, mi_template, mi_template2, condicionales_y_bucles, crear_auto, inicio
from django.urls import path

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('fecha-y-hora/', fecha_y_hora, name='fecha_y_hora'),
    path('mi-template/', mi_template, name='mi_template'),
    path('mi-template2/', mi_template2, name='mi_template2'),
    path('condicionales-y-bucles/', condicionales_y_bucles, name='condicionales_y_bucles'),
    path('crear-auto/<str:marca>/<str:modelo>/<int:anio>/', crear_auto, name='crear_auto'),
]
