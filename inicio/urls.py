from inicio.views import bienvenida, fecha_y_hora, saludo, mi_template, mi_template2, condicionales_y_bucles, crear_auto
from django.urls import path


urlpatterns = [
    path('bienvenida/', bienvenida),
    path('saludo/<str:nombre>/<str:apellido>/', saludo),
    path('fecha-y-hora/', fecha_y_hora),
    path('mi-template/', mi_template),
    path('mi-template2/', mi_template2),
    path('condicionales-y-bucles/', condicionales_y_bucles),
    path('crear-auto/', crear_auto),
]
