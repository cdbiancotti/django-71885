from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from mensajeria.models import Mensaje
from django.db.models import Q
from django.views.generic.edit import CreateView
from mensajeria.forms import EnviarMensajeFormulario
from django.urls import reverse_lazy


# @login_required
# def enviar_mensaje(request):
#     return render(request, 'mensajeria/enviar_mensaje.html', {})

class EnviarMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = EnviarMensajeFormulario
    success_url = reverse_lazy('mensajeria:listar_mensajes')
    template_name = 'mensajeria/enviar_mensaje.html'
    
    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)
    

@login_required
def ver_mensaje(request, mensaje_id):
    
    mensaje = Mensaje.objects.get(id=mensaje_id)
    
    return render(request, 'mensajeria/ver_mensaje.html', {'mensaje':mensaje})

@login_required
def listar_mensajes(request):
    
    recibidos = Mensaje.objects.filter(receptor=request.user)
    enviados = Mensaje.objects.filter(emisor=request.user)
    
    todos_los_mensajes = Mensaje.objects.filter(Q(receptor=request.user) | Q(emisor=request.user))
    
    return render(
        request, 
        'mensajeria/listar_mensajes.html', 
        {
            'todos_los_mensajes': todos_los_mensajes, 
            'recibidos': recibidos, 
            'enviados': enviados
        }
    )

