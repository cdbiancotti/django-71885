from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context

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
    
    # v1
    archivo_abierto = open('templates\mi_template.html')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    #v2
    # with open('templates\mi_template.html') as archivo_abierto:
        # template = Template(archivo_abierto.read())
    
    contexto = Context({'nombre': 'Ricardo'})
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)