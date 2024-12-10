from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login

def login(request):
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.get_user()
            
            django_login(request, usuario)
            return redirect('inicio:inicio')
            
        
    
    return render(request, 'usuarios/iniciar_sesion.html', {'form': form})