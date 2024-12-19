from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=20)
    anio = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='paletas', null=True)
    
    def __str__(self):
        return f'Paleta({self.id}): {self.marca} - {self.anio}'