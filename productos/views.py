from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from productos.models import Paleta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from productos.forms import ActualizarPaletaFormulario


class Paletas(ListView):
    model = Paleta
    template_name = "productos/listado_paletas.html"
    context_object_name = 'listado_paletas'

class CrearPaleta(CreateView):
    model = Paleta
    template_name = "productos/crear_paleta.html"
    fields = ['marca', 'anio', 'fecha', 'imagen']
    success_url = reverse_lazy('productos:listado_paletas')

class VerPaleta(DetailView):
    model = Paleta
    template_name = "productos/ver_paleta.html"

class EditarPaleta(LoginRequiredMixin, UpdateView):
    model = Paleta
    template_name = "productos/editar_paleta.html"
    form_class = ActualizarPaletaFormulario
    # fields = ['marca', 'anio', 'imagen']
    success_url = reverse_lazy('productos:listado_paletas')

class EliminarPaleta(LoginRequiredMixin, DeleteView):
    model = Paleta
    template_name = "productos/eliminar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
