# from inicio.views import (
#     bienvenida, 
#     fecha_y_hora, 
#     saludo, 
#     mi_template, 
#     mi_template2,
#     condicionales_y_bucles,
#     crear_auto,
#     inicio,
#     listado_autos
# )
from inicio import views
from django.urls import path

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('saludo/<str:nombre>/<str:apellido>/', views.saludo, name='saludo'),
    path('fecha-y-hora/', views.fecha_y_hora, name='fecha_y_hora'),
    path('mi-template/', views.mi_template, name='mi_template'),
    path('mi-template2/', views.mi_template2, name='mi_template2'),
    path('condicionales-y-bucles/', views.condicionales_y_bucles, name='condicionales_y_bucles'),
    # path('crear-auto/<str:marca>/<str:modelo>/<int:anio>/', crear_auto, name='crear_auto'),
    path('autos/', views.listado_autos, name='listado_autos'),
    path('autos/crear/', views.crear_auto, name='crear_auto'),
    path('autos/<int:id_auto>/', views.ver_auto, name='ver_auto'),
    path('autos/<int:id_auto>/eliminar/', views.eliminar_auto, name='eliminar_auto'),
    path('autos/<int:id_auto>/editar/', views.editar_auto, name='editar_auto'),
]
