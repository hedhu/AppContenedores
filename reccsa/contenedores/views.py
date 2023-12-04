from django.shortcuts import render, get_object_or_404
from .models import FacturaSAP, Factura, Contenedor, Usuario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CreacionUsuario

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

    contenedores = {'TLLU7509779': {'status': 'success', 'message': 'OK', 'data': {'metadata': {'type': 'CT', 'number': 'TLLU7509779', 'sealine': 'MAEU', 'sealine_name': 'Maersk', 'status': 'IN_TRANSIT', 'updated_at': '2023-08-18 18:49:42', 'api_calls': {'total': 100, 'used': 2, 'remaining': 98}, 'unique_shipments': {'total': 0, 'used': 0, 'remaining': 0}}, 'locations': [{'id': 1, 'name': 'Arica', 'state': 'Region de Arica y Parinacota', 'country': 'Chile', 'country_code': 'CL', 'locode': 'CLARI', 'lat': -18.4746, 'lng': -70.29792, 'timezone': 'America/Santiago'}, {'id': 2, 'name': 'Newark', 'state': 'New Jersey', 'country': 'United States', 'country_code': 'US', 'locode': 'USEWR', 'lat': 40.73566, 'lng': -74.17237, 'timezone': 'America/New_York'}, {'id': 3, 'name': 'Balboa', 'state': 'Provincia de Panama', 'country': 'Panama', 'country_code': 'PA', 'locode': 'PABLB', 'lat': 8.94814, 'lng': -79.56672, 'timezone': 'America/Panama'}, {'id': 4, 'name': 'Manzanillo', 'state': 'Provincia de Veraguas', 'country': 'Panama', 'country_code': 'PA', 'locode': 'PAMIT', 'lat': 7.73806, 'lng': -81.14444, 'timezone': 'America/Panama'}], 'facilities': [{'id': 1, 'name': 'Contopsa Arica', 'country_code': 'CL', 'locode': 'CLARI', 'bic_code': 'CLARIYUCL', 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 2, 'name': 'Terminal Puerto Arica (TPA)', 'country_code': 'CL', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 3, 'name': 'Balboa Port Terminal', 'country_code': 'PA', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 4, 'name': 'Manzanillo Terminal', 'country_code': 'PA', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 5, 'name': 'Apm Terminal - Berth 88 E425', 'country_code': 'US', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}], 'route': {'prepol': {'location': 1, 'date': '2023-07-28 15:12:00', 'actual': True}, 'pol': {'location': 1, 'date': '2023-07-31 16:46:00', 'actual': True}, 'pod': {'location': 2, 'date': '2023-09-07 07:00:00', 'actual': False, 'predictive_eta': None}, 'postpod': {'location': 2, 'date': '2023-09-07 07:00:00', 'actual': False}}, 'vessels': [{'id': 1, 'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}, {'id': 2, 'name': 'MAERSK KENTUCKY', 'imo': 9193240, 'call_sign': '9V6172', 'mmsi': 563073800, 'flag': 'SG'}], 'containers': [{'number': 'TLLU7509779', 'iso_code': '45G1', 'size_type': "40' High Cube Dry", 'status': 'IN_TRANSIT', 'events': [{'order_id': 1, 'location': 1, 'facility': 1, 'description': 'Gate out', 'event_type': 'EQUIPMENT', 'event_code': 'GTOT', 'status': 'CEP', 'date': '2023-07-28 15:12:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 2, 'location': 1, 'facility': 2, 'description': 'Gate in', 'event_type': 'EQUIPMENT', 'event_code': 'GTIN', 'status': 'CGI', 'date': '2023-07-31 16:46:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 3, 'location': 1, 'facility': 2, 'description': 'Load', 'event_type': 'EQUIPMENT', 'event_code': 'LOAD', 'status': 'CLL', 'date': '2023-08-03 05:29:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': None, 'vessel': 1, 'voyage': '331N'}, {'order_id': 4, 'location': 1, 'facility': 2, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDL', 'date': '2023-08-03 11:07:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 5, 'location': 3, 'facility': 3, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAT', 'date': '2023-08-23 01:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 6, 'location': 3, 'facility': 3, 'description': 'RAIL_DEPARTURE', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'LTS', 'date': '2023-08-26 16:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}, {'order_id': 7, 'location': 4, 'facility': 4, 'description': 'RAIL_ARRIVAL_AT_DESTINATION', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'LTS', 'date': '2023-08-26 17:30:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}, {'order_id': 8, 'location': 4, 'facility': 4, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDT', 'date': '2023-08-31 05:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 2, 'voyage': '335N'}, {'order_id': 9, 'location': 2, 'facility': 5, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAD', 'date': '2023-09-07 07:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 2, 'voyage': '335N'}]}], 'route_data': {'route': [{'path': [[-18.4746, -70.2979], [-18.4746, -70.2979], [-18.4744, -70.3007], [-18.4729, -70.3026], [-18.4703, -70.3035], [-18.4614, -70.3046], [-18.4479, -70.3081], [-18.4366, -70.3151], [-18.4276, -70.3257], [-15.4181, -75.1244], [-15.4099, -75.1366], [-15.4009, -75.1481], [-15.391, -75.159], [-14.6736, -75.8964], [-14.6603, -75.909], [-14.6463, -75.9206], [-14.6313, -75.9311], [-13.9308, -76.3837], [-13.9154, -76.3936], [-13.8998, -76.4033], [-13.8841, -76.4128], [-6.0021, -81.1384], [-5.9866, -81.1462], [-5.9702, -81.1513], [-5.953, -81.1537], [-4.2978, -81.2539], [-4.2811, -81.2544], [-4.2645, -81.2541], [-4.2479, -81.2528], [-1.0793, -80.9139], [-1.0628, -80.9121], [-1.0462, -80.9101], [-1.0296, -80.9079], [2.139477906118632, -80.4751048342792], [8.9266, -79.5482], [8.9374, -79.5482], [8.9472, -79.5512], [8.9562, -79.5571], [8.947, -79.549], [8.9513, -79.5546], [8.9517, -79.5604], [8.9483, -79.5665], [8.9481, -79.5667]], 'type': 'SEA', 'transport_type': 'VESSEL'}, {'path': [[8.94814, -79.56672], [10.09072, -83.5068], [10.09072, -83.5068], [7.73806, -81.14444]], 'type': 'LAND', 'transport_type': 'RAIL'}, {'path': [[7.73806, -81.14444], [7.65819685, -81.1062782], [7.285502149999999, -80.9281898], [7.205639, -80.890028], [7.210768099999999, -80.82246965], [7.2347039, -80.50719735], [7.239833, -80.439639], [7.28132885, -80.37256395], [7.47497615, -80.05954705], [7.516472, -79.992472], [7.73054345, -79.92549055], [8.729543549999999, -79.61291045], [8.943615, -79.545929], [9.0070242, -79.59980015], [9.3029338, -79.85119885], [9.366343, -79.90507], [10.99826245, -79.0407511], [18.61388655, -75.0072629], [20.245806, -74.142944], [20.6334309, -74.1740732], [22.442347100000003, -74.3193428], [22.829972, -74.350472], [22.830351200000003, -74.35046779999999], [22.8321208, -74.35044819999999], [22.8325, -74.350444], [25.372620849999997, -74.31244824999999], [37.22651815, -74.13513474999999], [39.766639, -74.097139], [39.877993149999995, -74.1262015], [40.39764585, -74.26182650000001], [40.509, -74.290889], [40.53003264103609, -74.26324561522937], [40.628184965871135, -74.13424315296635], [40.64921760690722, -74.10659976819571], [40.66218396587114, -74.11646530296635], [40.72269364103609, -74.16250446522936], [40.73566, -74.17237]], 'type': 'SEA', 'transport_type': 'VESSEL'}], 'pin': [2.139477906118632, -80.4751048342792], 'ais': {'status': 'OK', 'data': {'last_event': {'description': 'Vessel departure', 'date': '2023-08-03 11:07:00', 'voyage': '331N'}, 'discharge_port': {'name': 'Newark', 'country_code': 'US', 'code': 'EWR', 'date': '2023-09-07 07:00:00', 'date_label': 'ETA'}, 'vessel': {'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}, 'last_vessel_position': {'lat': -13.31337, 'lng': -77.02885, 'updated_at': '2023-08-18 18:44:58'}, 'departure_port': {'country_code': 'CL', 'code': 'VAP', 'date': '2023-08-14 22:18:00', 'date_label': 'ATD'}, 'arrival_port': {'country_code': 'PE', 'code': 'CLL', 'date': '2023-08-18 21:00:00', 'date_label': 'ETA'}, 'updated_at': '2023-08-18 18:49:43'}}}}}, 'MRSU6156065': {'status': 'success', 'message': 'OK', 'data': {'metadata': {'type': 'CT', 'number': 'MRSU6156065', 'sealine': 'MAEU', 'sealine_name': 'Maersk', 'status': 'IN_TRANSIT', 'updated_at': '2023-08-18 18:49:45', 'api_calls': {'total': 100, 'used': 3, 'remaining': 97}, 'unique_shipments': {'total': 0, 'used': 0, 'remaining': 0}}, 'locations': [{'id': 1, 'name': 'Arica', 'state': 'Region de Arica y Parinacota', 'country': 'Chile', 'country_code': 'CL', 'locode': 'CLARI', 'lat': -18.4746, 'lng': -70.29792, 'timezone': 'America/Santiago'}, {'id': 2, 'name': 'Los Angeles', 'state': 'California', 'country': 'United States', 'country_code': 'US', 'locode': 'USLAX', 'lat': 34.05223, 'lng': -118.24368, 'timezone': 'America/Los_Angeles'}, {'id': 3, 'name': 'Balboa', 'state': 'Provincia de Panama', 'country': 'Panama', 'country_code': 'PA', 'locode': 'PABLB', 'lat': 8.94814, 'lng': -79.56672, 'timezone': 'America/Panama'}], 'facilities': [{'id': 1, 'name': 'Contopsa Arica', 'country_code': 'CL', 'locode': 'CLARI', 'bic_code': 'CLARIYUCL', 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 2, 'name': 'Terminal Puerto Arica (TPA)', 'country_code': 'CL', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 3, 'name': 'Balboa Port Terminal', 'country_code': 'PA', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 4, 'name': 'LSA APM Terminal Pier 400( W185 )', 'country_code': 'US', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}], 'route': {'prepol': {'location': 1, 'date': '2023-07-31 09:50:00', 'actual': True}, 'pol': {'location': 1, 'date': '2023-07-31 16:53:00', 'actual': True}, 'pod': {'location': 2, 'date': '2023-09-07 08:00:00', 'actual': False, 'predictive_eta': None}, 'postpod': {'location': 2, 'date': '2023-09-07 08:00:00', 'actual': False}}, 'vessels': [{'id': 1, 'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}], 'containers': [{'number': 'MRSU6156065', 'iso_code': '42G0', 'size_type': "40' Dry Standard", 'status': 'IN_TRANSIT', 'events': [{'order_id': 1, 'location': 1, 'facility': 1, 'description': 'Gate out', 'event_type': 'EQUIPMENT', 'event_code': 'GTOT', 'status': 'CEP', 'date': '2023-07-31 09:50:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 2, 'location': 1, 'facility': 2, 'description': 'Gate in', 'event_type': 'EQUIPMENT', 'event_code': 'GTIN', 'status': 'CGI', 'date': '2023-07-31 16:53:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 3, 'location': 1, 'facility': 2, 'description': 'Load', 'event_type': 'EQUIPMENT', 'event_code': 'LOAD', 'status': 'CLL', 'date': '2023-08-03 05:28:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': None, 'vessel': 1, 'voyage': '331N'}, {'order_id': 4, 'location': 1, 'facility': 2, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDL', 'date': '2023-08-03 11:07:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 5, 'location': 3, 'facility': 3, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAT', 'date': '2023-08-23 01:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 6, 'location': 3, 'facility': 3, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDT', 'date': '2023-08-25 02:30:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': None, 'voyage': '334N'}, {'order_id': 7, 'location': 2, 'facility': 4, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAD', 'date': '2023-09-07 08:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': None, 'voyage': '334N'}]}], 'route_data': {'route': [{'path': [[-18.4746, -70.2979], [-18.4746, -70.2979], [-18.4744, -70.3007], [-18.4729, -70.3026], [-18.4703, -70.3035], [-18.4614, -70.3046], [-18.4479, -70.3081], [-18.4366, -70.3151], [-18.4276, -70.3257], [-15.4181, -75.1244], [-15.4099, -75.1366], [-15.4009, -75.1481], [-15.391, -75.159], [-14.6736, -75.8964], [-14.6603, -75.909], [-14.6463, -75.9206], [-14.6313, -75.9311], [-13.9308, -76.3837], [-13.9154, -76.3936], [-13.8998, -76.4033], [-13.8841, -76.4128], [-6.0021, -81.1384], [-5.9866, -81.1462], [-5.9702, -81.1513], [-5.953, -81.1537], [-4.2978, -81.2539], [-4.2811, -81.2544], [-4.2645, -81.2541], [-4.2479, -81.2528], [-1.0793, -80.9139], [-1.0628, -80.9121], [-1.0462, -80.9101], [-1.0296, -80.9079], [2.139515155302581, -80.47509974722635], [8.9266, -79.5482], [8.9374, -79.5482], [8.9472, -79.5512], [8.9562, -79.5571], [8.947, -79.549], [8.9513, -79.5546], [8.9517, -79.5604], [8.9483, -79.5665], [8.9481, -79.5667]], 'type': 'SEA', 'transport_type': 'VESSEL'}, {'path': [[8.9481, -79.5667], [8.949350519385787, -79.56528959643536], [8.955186276519461, -79.55870771313374], [8.95643679590525, -79.55729730956911], [8.954513526519461, -79.55559206313374], [8.945538269385787, -79.54763424643536], [8.943615, -79.545929], [8.729543549999999, -79.61291045], [7.73054345, -79.92549055], [7.516472, -79.992472], [7.47497615, -80.05954705], [7.28132885, -80.37256395], [7.239833, -80.439639], [7.2347039, -80.50719735], [7.210768099999999, -80.82246965], [7.205639, -80.890028], [7.259372299999999, -81.01439884999999], [7.5101277, -81.59479615000001], [7.563861, -81.719167], [7.63426515, -81.89519605000001], [7.96281785, -82.71666495], [8.033222, -82.892694], [9.57513875, -85.98527745], [16.77075025, -100.41733355000001], [18.312667, -103.509917], [18.9996253, -104.48474195], [22.2054307, -109.03392505000001], [22.892389, -110.00875], [23.1806473, -110.33384995], [24.5258527, -111.85098305], [24.814111, -112.176083], [25.2530569, -112.60369145], [27.3014711, -114.59919754999999], [27.740417, -115.026806], [28.56749195, -115.38803929999999], [32.427175049999995, -117.0737947], [33.25425, -117.435028], [33.35152405216108, -117.57222383934561], [33.80546962891281, -118.21247108962514], [33.9027436810739, -118.34966692897076], [33.92516212891282, -118.33377188962514], [34.02978155216108, -118.25959503934561], [34.0522, -118.2437]], 'type': 'SEA', 'transport_type': 'VESSEL'}], 'pin': [2.139515155302581, -80.47509974722635], 'ais': {'status': 'OK', 'data': {'last_event': {'description': 'Vessel departure', 'date': '2023-08-03 11:07:00', 'voyage': '331N'}, 'discharge_port': {'name': 'Los Angeles', 'country_code': 'US', 'code': 'LAX', 'date': '2023-09-07 08:00:00', 'date_label': 'ETA'}, 'vessel': {'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}, 'last_vessel_position': {'lat': -13.31337, 'lng': -77.02885, 'updated_at': '2023-08-18 18:44:58'}, 'departure_port': {'country_code': 'CL', 'code': 'VAP', 'date': '2023-08-14 22:18:00', 'date_label': 'ATD'}, 'arrival_port': {'country_code': 'PE', 'code': 'CLL', 'date': '2023-08-18 21:00:00', 'date_label': 'ETA'}, 'updated_at': '2023-08-18 18:49:44'}}}}}, 'TCKU7385121': {'status': 'success', 'message': 'OK', 'data': {'metadata': {'type': 'CT', 'number': 'TCKU7385121', 'sealine': 'MAEU', 'sealine_name': 'Maersk', 'status': 'IN_TRANSIT', 'updated_at': '2023-08-18 18:49:46', 'api_calls': {'total': 100, 'used': 3, 'remaining': 97}, 'unique_shipments': {'total': 0, 'used': 0, 'remaining': 0}}, 'locations': [{'id': 1, 'name': 'Arica', 'state': 'Region de Arica y Parinacota', 'country': 'Chile', 'country_code': 'CL', 'locode': 'CLARI', 'lat': -18.4746, 'lng': -70.29792, 'timezone': 'America/Santiago'}, {'id': 2, 'name': 'Chicago', 'state': 'Illinois', 'country': 'United States', 'country_code': 'US', 'locode': 'USCHI', 'lat': 41.85003, 'lng': -87.65005, 'timezone': 'America/Chicago'}, {'id': 3, 'name': 'Balboa', 'state': 'Provincia de Panama', 'country': 'Panama', 'country_code': 'PA', 'locode': 'PABLB', 'lat': 8.94814, 'lng': -79.56672, 'timezone': 'America/Panama'}, {'id': 4, 'name': 'Manzanillo', 'state': 'Provincia de Veraguas', 'country': 'Panama', 'country_code': 'PA', 'locode': 'PAMIT', 'lat': 7.73806, 'lng': -81.14444, 'timezone': 'America/Panama'}, {'id': 5, 'name': 'Newark', 'state': 'New Jersey', 'country': 'United States', 'country_code': 'US', 'locode': 'USEWR', 'lat': 40.73566, 'lng': -74.17237, 'timezone': 'America/New_York'}], 'facilities': [{'id': 1, 'name': 'Contopsa Arica', 'country_code': 'CL', 'locode': 'CLARI', 'bic_code': 'CLARIYUCL', 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 2, 'name': 'Terminal Puerto Arica (TPA)', 'country_code': 'CL', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 3, 'name': 'Balboa Port Terminal', 'country_code': 'PA', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 4, 'name': 'Manzanillo Terminal', 'country_code': 'PA', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 5, 'name': 'Apm Terminal - Berth 88 E425', 'country_code': 'US', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 6, 'name': 'Elizabeth Marine TE', 'country_code': 'US', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}, {'id': 7, 'name': 'Chicago CSX 59th Street Ramp', 'country_code': 'US', 'locode': None, 'bic_code': None, 'smdg_code': None, 'lat': None, 'lng': None}], 'route': {'prepol': {'location': 1, 'date': '2023-07-28 15:10:00', 'actual': True}, 'pol': {'location': 1, 'date': '2023-07-31 10:56:00', 'actual': True}, 'pod': {'location': 5, 'date': '2023-09-09 22:00:00', 'actual': False, 'predictive_eta': None}, 'postpod': {'location': 2, 'date': '2023-09-09 22:00:00', 'actual': False}}, 'vessels': [{'id': 1, 'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}, {'id': 2, 'name': 'MAERSK KENTUCKY', 'imo': 9193240, 'call_sign': '9V6172', 'mmsi': 563073800, 'flag': 'SG'}], 'containers': [{'number': 'TCKU7385121', 'iso_code': '42G0', 'size_type': "40' Dry Standard", 'status': 'IN_TRANSIT', 'events': [{'order_id': 1, 'location': 1, 'facility': 1, 'description': 'Gate out', 'event_type': 'EQUIPMENT', 'event_code': 'GTOT', 'status': 'CEP', 'date': '2023-07-28 15:10:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 2, 'location': 1, 'facility': 2, 'description': 'Gate in', 'event_type': 'EQUIPMENT', 'event_code': 'GTIN', 'status': 'CGI', 'date': '2023-07-31 10:56:00', 'actual': True, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 3, 'location': 1, 'facility': 2, 'description': 'Load', 'event_type': 'EQUIPMENT', 'event_code': 'LOAD', 'status': 'CLL', 'date': '2023-08-03 05:30:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': None, 'vessel': 1, 'voyage': '331N'}, {'order_id': 4, 'location': 1, 'facility': 2, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDL', 'date': '2023-08-03 11:07:00', 'actual': True, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 5, 'location': 3, 'facility': 3, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAT', 'date': '2023-08-23 01:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 1, 'voyage': '331N'}, {'order_id': 6, 'location': 3, 'facility': 3, 'description': 'RAIL_DEPARTURE', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'LTS', 'date': '2023-08-26 16:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}, {'order_id': 7, 'location': 4, 'facility': 4, 'description': 'RAIL_ARRIVAL_AT_DESTINATION', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'LTS', 'date': '2023-08-26 17:30:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}, {'order_id': 8, 'location': 4, 'facility': 4, 'description': 'Vessel departure', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'VDT', 'date': '2023-08-31 05:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 2, 'voyage': '335N'}, {'order_id': 9, 'location': 5, 'facility': 5, 'description': 'Vessel arrival', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'VAD', 'date': '2023-09-07 07:00:00', 'actual': False, 'is_additional_event': False, 'type': 'sea', 'transport_type': 'VESSEL', 'vessel': 2, 'voyage': '335N'}, {'order_id': 10, 'location': 5, 'facility': 5, 'description': 'Gate out', 'event_type': 'EQUIPMENT', 'event_code': 'GTOT', 'status': 'LTS', 'date': '2023-09-07 23:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 11, 'location': 5, 'facility': 6, 'description': 'Gate in', 'event_type': 'EQUIPMENT', 'event_code': 'GTIN', 'status': 'LTS', 'date': '2023-09-08 23:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': None, 'vessel': None, 'voyage': None}, {'order_id': 12, 'location': 5, 'facility': 6, 'description': 'RAIL_DEPARTURE', 'event_type': 'TRANSPORT', 'event_code': 'DEPA', 'status': 'LTS', 'date': '2023-09-08 23:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}, {'order_id': 13, 'location': 2, 'facility': 7, 'description': 'RAIL_ARRIVAL_AT_DESTINATION', 'event_type': 'TRANSPORT', 'event_code': 'ARRI', 'status': 'LTS', 'date': '2023-09-09 22:00:00', 'actual': False, 'is_additional_event': False, 'type': 'land', 'transport_type': 'RAIL', 'vessel': None, 'voyage': None}]}], 'route_data': {'route': [{'path': [[-18.4746, -70.2979], [-18.4746, -70.2979], [-18.4744, -70.3007], [-18.4729, -70.3026], [-18.4703, -70.3035], [-18.4614, -70.3046], [-18.4479, -70.3081], [-18.4366, -70.3151], [-18.4276, -70.3257], [-15.4181, -75.1244], [-15.4099, -75.1366], [-15.4009, -75.1481], [-15.391, -75.159], [-14.6736, -75.8964], [-14.6603, -75.909], [-14.6463, -75.9206], [-14.6313, -75.9311], [-13.9308, -76.3837], [-13.9154, -76.3936], [-13.8998, -76.4033], [-13.8841, -76.4128], [-6.0021, -81.1384], [-5.9866, -81.1462], [-5.9702, -81.1513], [-5.953, -81.1537], [-4.2978, -81.2539], [-4.2811, -81.2544], [-4.2645, -81.2541], [-4.2479, -81.2528], [-1.0793, -80.9139], [-1.0628, -80.9121], [-1.0462, -80.9101], [-1.0296, -80.9079], [2.139552404486529, -80.47509466017353], [8.9266, -79.5482], [8.9374, -79.5482], [8.9472, -79.5512], [8.9562, -79.5571], [8.947, -79.549], [8.9513, -79.5546], [8.9517, -79.5604], [8.9483, -79.5665], [8.9481, -79.5667]], 'type': 'SEA', 'transport_type': 'VESSEL'}, {'path': [[8.94814, -79.56672], [10.09072, -83.5068], [10.09072, -83.5068], [7.73806, -81.14444]], 'type': 'LAND', 'transport_type': 'RAIL'}, {'path': [[7.73806, -81.14444], [7.65819685, -81.1062782], [7.285502149999999, -80.9281898], [7.205639, -80.890028], [7.210768099999999, -80.82246965], [7.2347039, -80.50719735], [7.239833, -80.439639], [7.28132885, -80.37256395], [7.47497615, -80.05954705], [7.516472, -79.992472], [7.73054345, -79.92549055], [8.729543549999999, -79.61291045], [8.943615, -79.545929], [9.0070242, -79.59980015], [9.3029338, -79.85119885], [9.366343, -79.90507], [10.99826245, -79.0407511], [18.61388655, -75.0072629], [20.245806, -74.142944], [20.6334309, -74.1740732], [22.442347100000003, -74.3193428], [22.829972, -74.350472], [22.830351200000003, -74.35046779999999], [22.8321208, -74.35044819999999], [22.8325, -74.350444], [25.372620849999997, -74.31244824999999], [37.22651815, -74.13513474999999], [39.766639, -74.097139], [39.877993149999995, -74.1262015], [40.39764585, -74.26182650000001], [40.509, -74.290889], [40.53003264103609, -74.26324561522937], [40.628184965871135, -74.13424315296635], [40.64921760690722, -74.10659976819571], [40.66218396587114, -74.11646530296635], [40.72269364103609, -74.16250446522936], [40.73566, -74.17237]], 'type': 'SEA', 'transport_type': 'VESSEL'}, {'path': [[40.73566, -74.17237], [40.7082, -74.09215], [40.508, -74.70855], [40.66472, -75.23556], [40.43389, -75.88806], [40.34028, -75.95], [40.36611, -76.31222], [40.26222, -76.78528], [40.54462, -77.21221], [40.51423, -77.34954], [40.589, -77.46386], [40.41736, -77.82464], [40.65889, -78.26972], [40.38583, -78.68611], [40.31333, -79.54945], [40.57746, -80.20116], [40.81913, -80.37296], [40.91389, -80.88889], [40.78856, -81.38628], [40.83712, -81.84598], [40.65974, -82.15038], [40.81083, -82.59445], [40.78526, -84.20438], [41.07215, -85.14226], [41.465, -87.05472], [41.88361, -87.75617], [41.85003, -87.65005]], 'type': 'LAND', 'transport_type': 'RAIL'}], 'pin': [2.139552404486529, -80.47509466017353], 'ais': {'status': 'OK', 'data': {'last_event': {'description': 'Vessel departure', 'date': '2023-08-03 11:07:00', 'voyage': '331N'}, 'discharge_port': {'name': 'Newark', 'country_code': 'US', 'code': 'EWR', 'date': '2023-09-09 22:00:00', 'date_label': 'ETA'}, 'vessel': {'name': 'POLAR COLOMBIA', 'imo': 9786762, 'call_sign': '9V6726', 'mmsi': 563103200, 'flag': 'SG'}, 'last_vessel_position': {'lat': -13.31337, 'lng': -77.02885, 'updated_at': '2023-08-18 18:44:58'}, 'departure_port': {'country_code': 'CL', 'code': 'VAP', 'date': '2023-08-14 22:18:00', 'date_label': 'ATD'}, 'arrival_port': {'country_code': 'PE', 'code': 'CLL', 'date': '2023-08-18 21:00:00', 'date_label': 'ETA'}, 'updated_at': '2023-08-18 18:49:44'}}}}}}

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
    
