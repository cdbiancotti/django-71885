from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', views.login, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),
]
