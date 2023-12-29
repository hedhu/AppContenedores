from celery import shared_task
from .models import FacturaSAP, Factura, Contenedor
import json, requests
from decouple import config

@shared_task
def actualizarBaseDeDatos():
    try:
        container_ids = []
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
            container_ids.append(factura.U_CONTAINER)
            nuevaFactura.save()
        facturasCerradas = Factura.objects.exclude(DocNum__in = [factura.DocNum for factura in facturasAbiertas])
        for factura in facturasCerradas:
            factura.U_ESTADO_CONTENEDOR = "CERRADO"
            factura.save()
    except Exception as e:
        print(f"Se produjo un error: {e}")

    params = {
        "api_key": config('API_KEY'),
        "number": None, 
        "sealine": "auto",
        "type": "CT",
        "force_update": False,
        "route": True,
        "ais": True
    }
    
    url = "https://tracking.searates.com/tracking"
    contenedores = {} 

    for container_id in container_ids:
        params["number"] = container_id
        response = requests.get(url, params=params)
        data = response.json()
        contenedores[container_id] = data


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

@shared_task
def sleepTest():
    return "FUNCIONA"
     