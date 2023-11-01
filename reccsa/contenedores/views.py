from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# def home(request):
#     return render(request, 'contenedores/buscador.html')

# @login_required
def buscador(request):
    usuario = request.POST.get('username')
    contraseña = request.POST.get('password')
    print(usuario, contraseña)
    return render(request, 'contenedores/buscador.html')

def contenedor(request):
    return render(request, 'contenedores/contenedor.html')