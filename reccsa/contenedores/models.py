from django.contrib.auth.models import AbstractUser
from django.db import models

class Contenedor(models.Model):
    codigo = models.CharField(max_length=30, primary_key=True)
    naviera_nom = models.CharField(max_length=45, null=True)
    estado = models.CharField(max_length=30, null=True)
    ultimo_evento_desc = models.CharField(max_length=150, null=True)
    ultimo_evento_fecha = models.DateTimeField(null=True)
    id_viaje = models.CharField(max_length=30, null=True)
    puerto_descarga_eta = models.DateTimeField(null=True)
    puerto_descarga_nom = models.CharField(max_length=50, null=True)
    puerto_descarga_cod_pais = models.CharField(max_length=10, null=True)
    puerto_descarga_cod = models.CharField(max_length=10, null=True)
    buque_nom = models.CharField(max_length=50, null=True)
    buque_imo = models.CharField(max_length=30, null=True)
    buque_mmsi = models.CharField(max_length=30,null=True)
    buque_flag = models.CharField(max_length=10, null=True)
    buque_lat = models.FloatField(null=True)
    buque_lng = models.FloatField(null=True)
    buque_ult_actualizacion = models.DateTimeField(null=True)
    puerto_salida_atd = models.DateTimeField(null=True)
    puerto_salida_cod_pais = models.CharField(max_length=10, null=True)
    puerto_salida_cod = models.CharField(max_length=10, null=True)
    puerto_llegada_eta = models.DateTimeField(null=True)
    puerto_llegada_cod_pais = models.CharField(max_length=10, null=True)
    puerto_llegada_cod = models.CharField(max_length=10, null=True)
    ultima_actualizacion_tracking = models.DateTimeField(null=True)
    ultima_actualizacion_modelo = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.codigo} | {self.estado} | {self.ultima_actualizacion_modelo}'


class FacturaSAP(models.Model):
    DocNum = models.IntegerField(primary_key=True)
    DocDate = models.DateTimeField()
    U_CONTAINER = models.CharField(max_length=100)
    U_FECHA_BL = models.DateField()
    CardName = models.CharField(max_length=100)
    CardCode = models.CharField(max_length=100)
    U_ESTADO_CONTENEDOR = models.CharField(max_length=50)

    class Meta:
        db_table = 'contenedorestransito'
        managed = False

    def __str__(self):
        return f'{self.DocNum} {self.CardName}'
    
class Factura(models.Model):
    DocNum = models.IntegerField(primary_key=True)
    DocDate = models.DateTimeField(null=True)
    U_CONTAINER = models.CharField(max_length=100)
    U_FECHA_BL = models.DateTimeField(null=True)
    CardCode = models.CharField(max_length=100)
    CardName = models.CharField(max_length=100)
    U_ESTADO_CONTENEDOR = models.CharField(max_length=50)
    Contenedor = models.OneToOneField(Contenedor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.DocNum} | {self.CardName} '
