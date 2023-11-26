from celery import shared_task
from .models import FacturaSAP, Factura
import django

@shared_task
def actualizarBaseDeDatos():
    
    # # Parámetros de conexión
    # server = 'localhost:3306'
    # database = 'TST13_CONDENSA'
    # username = 'SA'
    # password = 'Sa123456'

    # # String de conexión
    # conn_str = (
    #     r'DRIVER={{MySQL ODBC 8.0 Driver}}'
    #     f'SERVER={server};'
    #     f'DATABASE={database};'
    #     f'UID={username};'
    #     f'PWD={password}'
    # )

    # # Conectar a la base de datos
    # conn = pyodbc.connect(conn_str)

    # cursor = conn.cursor()
    # query = 'SELECT U_CONTAINER FROM ContenedoresTransito'
    # cursor.execute(query)
    # container_ids= [row[0] for row in cursor.fetchall()] 

    # cursor.close()

    # cursor = conn.cursor()
    # querytodo= 'SELECT * FROM ContenedoresTransito'
    # cursor.execute(querytodo)
    # facturas = cursor.fetchall()

    # conn.close()

    django.setup()

    try:
        facturas = FacturaSAP.objects.filter(U_ESTADO_CONTENEDOR = "ABIERTO").using("bd_sap")
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
        raise

    # url = "https://tracking.searates.com/tracking"

    # params = {
    #     "api_key": "QMG5-9V1O-W8AD-07TL-N4Y6",
    #     "number": None,  # We will update this for each request
    #     "sealine": "auto",
    #     "type": "CT",
    #     "force_update": False,
    #     "route": True,
    #     "ais": True
    # }

    # all_data = {}  # A dictionary to hold the data for all containers

    # for container_id in container_ids:
    #     params["number"] = container_id
    #     response = requests.get(url, params=params)
    #     data = response.json()
    #     all_data[container_id] = data

    # # Convert the data to a JSON-formatted string with indentation
    # formatted_data = json.dumps(all_data, indent=4)

    # # Write the formatted data to a text file
    # # with open("datanueva.json", "w") as file:
    # #     file.write(formatted_data)

    # return(formatted_data)

@shared_task
def sleepTest():
    return "FUNCIONA"
     