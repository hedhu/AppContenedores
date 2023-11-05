from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tasks import sleepTest

# Create your views here.
# def home(request):
#     return render(request, 'contenedores/buscador.html')

# @login_required
def buscador(request):
    sleepTest.delay()
    usuario = request.POST.get('username')
    contraseña = request.POST.get('password')
    print(usuario, contraseña)
    return render(request, 'contenedores/buscador.html')

def contenedor(request):
    return render(request, 'contenedores/contenedor.html')