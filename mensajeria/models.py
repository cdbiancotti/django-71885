from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisores')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptores')
    mensaje = models.CharField(max_length=500)
    fecha = models.DateTimeField()
    
    def __str__(self):
        return f'Mensaje de {self.emisor} a {self.receptor} - {self.fecha}'