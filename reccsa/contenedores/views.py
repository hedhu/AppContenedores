from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from .models import FacturaSAP, Factura, Contenedor, Usuario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from .forms import CreacionUsuario
import json

def index(request):
    return render(request, 'contenedores/index.html')

@method_decorator(login_required, name='dispatch')
class ContenedoresListView(ListView):
    model = Contenedor
    template_name = 'contenedores/buscador.html'
    context_object_name = 'contenedores'

@method_decorator(login_required, name='dispatch')
class ContenedorDetailView(DetailView):
    model = Contenedor
    template_name = 'contenedores/contenedor.html'
    context_object_name = 'contenedor'
    slug_field = 'codigo'
    slug_url_kwarg = 'contenedor_codigo'

    def get_object(self, queryset=None):
        return get_object_or_404(Contenedor, codigo=self.kwargs['contenedor_codigo'])

@method_decorator(login_required, name='dispatch')
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'contenedores/usuario_lista.html'
    context_object_name = 'usuarios'

@method_decorator(login_required, name='dispatch')
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = CreacionUsuario
    template_name = 'contenedores/usuario_crear.html'
    success_url = reverse_lazy('usuario_lista')

    def form_valid(self, form):
        group = form.cleaned_data['perfil']
        user = form.save()
        user.groups.set([group])
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'contenedores/usuario_eliminar.html' 
    success_url = reverse_lazy('usuario_lista') 
    

def temporal(request):

    with open('C:/Users/edvva/OneDrive/Escritorio/Carpetas/AppContenedores/reccsa/contenedores/datanueva.json', 'r') as file:
        contenedores = json.load(file)
        print(contenedores)
    
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

    for idContenedor, dataContenedor in contenedores.items():
        aisDataContenedor = dataContenedor["data"]["route_data"]["ais"]["data"]

        nuevoContenedor, creado = Contenedor.objects.get_or_create(codigo = idContenedor)

        nuevoContenedor.naviera_nom = dataContenedor["data"]["metadata"]["sealine_name"]

        nuevoContenedor.estado = dataContenedor["data"]["containers"][0]["status"]

        nuevoContenedor.ultimo_evento_desc = aisDataContenedor["last_event"]["description"]
        nuevoContenedor.ultimo_evento_fecha = aisDataContenedor["last_event"]["date"]
        nuevoContenedor.id_viaje = aisDataContenedor["last_event"]["voyage"]

        nuevoContenedor.puerto_descarga_eta = aisDataContenedor["discharge_port"]["date"]
        nuevoContenedor.puerto_descarga_nom = aisDataContenedor["discharge_port"]["name"]
        nuevoContenedor.puerto_descarga_cod_pais = aisDataContenedor["discharge_port"]["country_code"]
        nuevoContenedor.puerto_descarga_cod = aisDataContenedor["discharge_port"]["code"]

        nuevoContenedor.buque_nom = aisDataContenedor["vessel"]["name"]
        nuevoContenedor.buque_imo = aisDataContenedor["vessel"]["imo"]
        nuevoContenedor.buque_mmsi = aisDataContenedor["vessel"]["mmsi"]
        nuevoContenedor.buque_flag = aisDataContenedor["vessel"]["flag"]
        nuevoContenedor.buque_lat = aisDataContenedor["last_vessel_position"]["lat"]
        nuevoContenedor.buque_lng = aisDataContenedor["last_vessel_position"]["lng"]
        nuevoContenedor.buque_ult_actualizacion = aisDataContenedor["last_vessel_position"]["updated_at"]

        nuevoContenedor.puerto_salida_atd = aisDataContenedor["departure_port"]["date"]
        nuevoContenedor.puerto_salida_cod_pais= aisDataContenedor["departure_port"]["country_code"]
        nuevoContenedor.puerto_salida_cod = aisDataContenedor["departure_port"]["code"]

        nuevoContenedor.puerto_llegada_eta = aisDataContenedor["arrival_port"]["date"]
        nuevoContenedor.puerto_llegada_cod_pais = aisDataContenedor["arrival_port"]["country_code"]
        nuevoContenedor.puerto_llegada_cod = aisDataContenedor["arrival_port"]["code"]

        nuevoContenedor.ultima_actualizacion_tracking = aisDataContenedor["updated_at"]

        nuevoContenedor.save()

        facturaContenedor = Factura.objects.get(U_CONTAINER=nuevoContenedor.codigo)
        facturaContenedor.Contenedor = nuevoContenedor
        facturaContenedor.save()

    context = { 'contenedores' : Contenedor.objects.all() }

    return render(request, 'contenedores/buscador.html', context)
    
# def contenedor(request, contenedor_codigo):
    # contenedor = get_object_or_404(Contenedor, codigo = contenedor_codigo)
    # return render(request, 'contenedores/contenedor.html', { 'contenedor': contenedor })

def list_contenedores(_request):
    contenedores = list(Contenedor.objects.values())
    facturas = list(Factura.objects.values())
    
    contenedores_data = []
    for contenedor in contenedores:
        factura_correspondiente = next((factura for factura in facturas if factura['U_CONTAINER'] == contenedor['codigo']), None)

        contenedor_data = {
            'codigo': contenedor['codigo'],
            'doc_num': factura_correspondiente['DocNum'] if factura_correspondiente else '-',
            'estado': contenedor['estado'],
            'ultima_actualizacion_tracking': contenedor['ultima_actualizacion_tracking'],
            'url_contenedor': reverse('contenedor', kwargs={'contenedor_codigo': contenedor['codigo']}),
        }

        contenedores_data.append(contenedor_data)

    data = {'contenedores': contenedores_data}
    return JsonResponse(data)
    