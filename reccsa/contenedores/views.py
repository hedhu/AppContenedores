from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FacturaSAP, Factura

# Create your views here.
# def home(request):
#     return render(request, 'contenedores/buscador.html')

# @login_required
def buscador(request):
    facturas = FacturaSAP.objects.filter(U_ESTADO_CONTENEDOR = "ABIERTO").using("bd_sap")
    try:
        for factura in facturas:
            nuevaFactura = Factura(
                DocNum = factura.DocNum,
                DocDate = factura.DocDate,
                U_CONTAINER = factura.U_CONTAINER,
                U_FECHA_BL = factura.U_FECHA_BL,
                CardName = factura.CardName,
                CardCode = factura.CardCode,
                U_ESTADO_CONTENEDOR = factura.U_ESTADO_CONTENEDOR
            )
            nuevaFactura.save()
    except Exception as e:
        print(f"Se produjo un error: {e}")
    

        
    
    print(list(facturas.values()))

    usuario = request.POST.get('username')
    contraseña = request.POST.get('password')
    print(usuario, contraseña)
    return render(request, 'contenedores/buscador.html')

def contenedor(request):

    return render(request, 'contenedores/contenedor.html')