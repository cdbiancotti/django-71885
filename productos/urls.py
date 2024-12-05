from django.urls import path
from productos import views

app_name = 'productos'

urlpatterns = [
    path('paletas/', views.VerPaleta.as_view(), name='listado_paletas')
]
