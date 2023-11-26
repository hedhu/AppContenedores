import json

rutaJson = "datacontenedor.json"

with open(rutaJson, 'r') as archivo_json:
    datos_dict = json.load(archivo_json)

print(datos_dict)