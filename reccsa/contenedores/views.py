from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import FacturaSAP, Factura, Contenedor, Usuario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CreacionUsuario
import json

def index(request):
    return render(request, 'contenedores/index.html')

@method_decorator(login_required, name='dispatch')
class ContenedoresListView(ListView):
    model = Contenedor
    template_name = 'contenedores/buscador.html'
    context_object_name = 'contenedores'

    def get_queryset(self):
        return Contenedor.objects.filter(factura__U_ESTADO_CONTENEDOR = "ABIERTO")

@method_decorator(login_required, name='dispatch')
class ContenedoresCerradosListView(ListView):
    model = Contenedor
    template_name = 'contenedores/buscador_cerrados.html'
    context_object_name = 'contenedores'

    def get_queryset(self):
        return Contenedor.objects.filter(factura__U_ESTADO_CONTENEDOR = "CERRADO")

@method_decorator(login_required, name='dispatch')
class ContenedorDetailView(DetailView):
    model = Contenedor
    template_name = 'contenedores/contenedor.html'
    context_object_name = 'contenedor'
    slug_field = 'codigo'
    slug_url_kwarg = 'contenedor_codigo'

    def get_object(self, queryset=None):
        return get_object_or_404(Contenedor, codigo=self.kwargs['contenedor_codigo'])


class UsuarioListView(UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'contenedores/usuario_lista.html'
    context_object_name = 'usuarios'

    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()

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
    
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()

@method_decorator(login_required, name='dispatch')
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'contenedores/usuario_eliminar.html' 
    success_url = reverse_lazy('usuario_lista') 
    
    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()


def temporal(request):

    with open('C:/Users/johnn/Desktop/reccsa/AppContenedores/reccsa/contenedores/datanueva.json', 'r') as file:
        contenedores = json.load(file)
        # print(contenedores)
    
    try:
        facturasAbiertas = FacturaSAP.objects.filter(U_ESTADO_CONTENEDOR = "ABIERTO").using("bd_sap")
        for factura in facturasAbiertas:
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
        facturasCerradas = Factura.objects.exclude(DocNum__in = [factura.DocNum for factura in facturasAbiertas])
        for factura in facturasCerradas:
            factura.U_ESTADO_CONTENEDOR = "CERRADO"
            factura.save()
    except Exception as e:
        print(f"Se produjo un error: {e}")

    for idContenedor, dataContenedor in contenedores.items():

        if dataContenedor["status"] == "success":
            if dataContenedor["data"]["route_data"]["ais"]["status"] == "OK":
                aisDataContenedor = dataContenedor["data"]["route_data"]["ais"]["data"]

                nuevoContenedor, creado = Contenedor.objects.get_or_create(codigo = idContenedor)

                nuevoContenedor.pol = dataContenedor["data"]["route"]["pol"]["date"]

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

            elif dataContenedor["data"]["route_data"]["ais"]["status"] == "NOT_ON_BOARD":
                nuevoContenedor, creado = Contenedor.objects.get_or_create(codigo = idContenedor)
                nuevoContenedor.estado = dataContenedor["data"]["route_data"]["ais"]["status"]
                nuevoContenedor.pol = dataContenedor["data"]["route"]["pol"]["date"]
                nuevoContenedor.ultima_actualizacion_tracking = dataContenedor["data"]["metadata"]["updated_at"]

                nuevoContenedor.save()

                facturaContenedor = Factura.objects.get(U_CONTAINER=nuevoContenedor.codigo)
                facturaContenedor.Contenedor = nuevoContenedor
                facturaContenedor.save()
        
        else:
            nuevoContenedor, creado = Contenedor.objects.get_or_create(codigo = idContenedor)
            nuevoContenedor.estado = dataContenedor["message"]

            nuevoContenedor.save()

            facturaContenedor = Factura.objects.get(U_CONTAINER=nuevoContenedor.codigo)
            facturaContenedor.Contenedor = nuevoContenedor
            facturaContenedor.save()

        

    context = { 'contenedores' : Contenedor.objects.all() }

    return render(request, 'contenedores/buscador.html', context)