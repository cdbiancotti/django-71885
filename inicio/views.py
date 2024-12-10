from datetime import datetime
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto
import random
from inicio.forms import CrearAuto, BuscarAuto, EditarAuto
from django.contrib.auth.decorators import login_required

def bienvenida(request):
    return render(request, 'inicio/bienvenida.html')

def inicio(request):
    return render(request, 'inicio/inicio.html')

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

    return render(request, 'inicio/mi_template.html', {'nombre': 'Ricardo'})


def mi_template2(request):
    # template = loader.get_template('mi_template2.html')
    
    # diccionario = {'nombre': 'Ricardo'}
    
    # template_renderizado = template.render(diccionario)
    
    # return HttpResponse(template_renderizado)

    return render(request, 'inicio/mi_template2.html', {})


def condicionales_y_bucles(request):
    
    return render(request, 'inicio/condicionales_y_bucles.html', {
        'nombre': 'Ricardo',
        'mis_elementos': [],
        'numero': 2,
        'numeros': list(range(15))
    })
    
    
# def crear_auto(request, marca, modelo, anio):
    
#     # auto = Auto(marca=random.choice(['Ford','Fiat','Chevrolet','Ferrari','Mercedes']), modelo='Generico', anio=random.choice([2020,2021,2022,2023,2024])) 
#     auto = Auto(marca=marca, modelo=modelo, anio=anio) 
#     auto.save()
    
#     return render(request, 'inicio/auto_creacion_correcta.html', {'auto': auto})

def crear_auto(request):
    # print('******************************************************')
    # print('Request', request)
    # print('GET', request.GET)
    # print('POST', request.POST)
    # print('******************************************************')
    
    formulario = CrearAuto()
    
    if request.method == 'POST':
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            
            auto = Auto(marca=data.get('marca'), modelo=data.get('modelo'), anio=data.get('anio'))
            auto.save()
            
            return redirect('inicio:listado_autos')
    
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def listado_autos(request):
    
    # marca_a_buscar = request.GET.get('marca')
    # modelo_a_buscar = request.GET.get('modelo')
    
    # v1
    # if marca_a_buscar:
    #     resultado_autos = Auto.objects.filter(marca__icontains=marca_a_buscar)
    # else:
    #     resultado_autos = Auto.objects.all()

    # v2
    # resultado_autos = Auto.objects.filter(marca__icontains=marca_a_buscar, modelo__icontains=modelo_a_buscar)
    
    formulario_busqueda = BuscarAuto(request.GET)
    
    if formulario_busqueda.is_valid():
        marca_a_buscar = formulario_busqueda.cleaned_data.get('marca')
        modelo_a_buscar = formulario_busqueda.cleaned_data.get('modelo')
        resultado_autos = Auto.objects.filter(marca__icontains=marca_a_buscar, modelo__icontains=modelo_a_buscar)
    else:
        resultado_autos = []

    formulario_busqueda = BuscarAuto()
    
    return render(request, 'inicio/listado_autos.html', {'listado_autos': resultado_autos, 'formulario': formulario_busqueda})

def ver_auto(request, id_auto):
    
    auto = Auto.objects.get(id=id_auto)
    
    return render(request, 'inicio/ver_auto.html', {'auto': auto})

@login_required
def eliminar_auto(request, id_auto):
    
    auto = Auto.objects.get(id=id_auto)
    
    auto.delete()
    
    return render(request, 'inicio/eliminar_auto.html', {'auto': auto})

@login_required
def editar_auto(request, id_auto):
    
    auto = Auto.objects.get(id=id_auto)
    
    formulario = EditarAuto(initial={'marca': auto.marca, 'modelo': auto.modelo, 'anio': auto.anio})
    
    if request.method == 'POST':
        formulario = EditarAuto(request.POST)
        if formulario.is_valid():
            
            auto.marca = formulario.cleaned_data.get('marca')
            auto.modelo = formulario.cleaned_data.get('modelo')
            auto.anio = formulario.cleaned_data.get('anio')
    
            auto.save()
            
            return redirect('inicio:listado_autos')
    
    return render(request, 'inicio/editar_auto.html', {'formulario': formulario, 'auto': auto})