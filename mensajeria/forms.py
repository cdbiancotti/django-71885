from django.forms import ModelForm
from mensajeria.models import Mensaje
from datetime import datetime

class EnviarMensajeFormulario(ModelForm):
    
    class Meta:
        model = Mensaje
        fields = ['receptor', 'mensaje']
    
    def save(self, commit = True):
        instancia_de_mensaje = super().save(commit=False)
        
        instancia_de_mensaje.fecha = datetime.now()
        
        if commit:
            instancia_de_mensaje.save()
        
        return instancia_de_mensaje