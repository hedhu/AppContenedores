from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def buscador(request):
    return render(request, 'contenedores/buscador.html')

def contenedor(request):
    return render(request, 'contenedores/contenedor.html')