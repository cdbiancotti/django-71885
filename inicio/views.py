from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto
import random

def bienvenida(request):
    return HttpResponse('<h1>Bienvenida!</h1>')

def fecha_y_hora(request):
    fecha_y_hora = datetime.now()
    
    # v1
    # return HttpResponse('<h1>Esta vista muestra la hora actual</h1>\nfecha_y_hora')
    
    # v2
#     return HttpResponse(f'''<h1>Esta vista muestra la hora actual</h1>
# {fecha_y_hora}''')
    
    # v3
    respuesta = f'''<h1>Esta vista muestra la hora actual</h1>
{fecha_y_hora}'''
    return HttpResponse(respuesta)

def saludo(request, nombre, apellido):
    nombre_formateado = nombre.title()
    apellido_formateado = apellido.title()
    return HttpResponse(f"Buenas {nombre_formateado} {apellido_formateado}, como va?")

def mi_template(request):
    
    # # v1
    # # archivo_abierto = open('templates\mi_template.html')
    # # archivo_abierto = open(r'C:\Users\cdbia\Desktop\proyectos-71885\django\templates\mi_template.html')
    # archivo_abierto = open('mi_template.html')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    # #v2
    # # with open('templates\mi_template.html') as archivo_abierto:
    #     # template = Template(archivo_abierto.read())
    
    # contexto = Context({'nombre': 'Ricardo'})
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado)

    return render(request, 'mi_template.html', {'nombre': 'Ricardo'})


def mi_template2(request):
    # template = loader.get_template('mi_template2.html')
    
    # diccionario = {'nombre': 'Ricardo'}
    
    # template_renderizado = template.render(diccionario)
    
    # return HttpResponse(template_renderizado)

    return render(request, 'mi_template2.html', {})


def condicionales_y_bucles(request):
    
    return render(request, 'condicionales_y_bucles.html', {
        'nombre': 'Ricardo',
        'mis_elementos': [],
        'numero': 2,
        'numeros': list(range(15))
    })
    
    
def crear_auto(request):
    
    auto = Auto(marca=random.choice(['Ford','Fiat','Chevrolet','Ferrari','Mercedes']), modelo='Generico', anio=random.choice([2020,2021,2022,2023,2024])) 
    auto.save()
    
    return render(request, 'auto_creacion_correcta.html', {})