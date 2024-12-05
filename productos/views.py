from django.shortcuts import render
from django.views.generic.list import ListView
from productos.models import Paleta


class VerPaleta(ListView):
    model = Paleta
    template_name = "productos/listado_paletas.html"
    context_object_name = 'listado_paletas'
