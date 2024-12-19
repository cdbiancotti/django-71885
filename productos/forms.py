
from django import forms
from productos.models import Paleta

class ActualizarPaletaFormulario(forms.ModelForm):
    
    class Meta:
        model = Paleta
        fields = ['marca']