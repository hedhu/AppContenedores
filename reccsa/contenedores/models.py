from django.contrib.auth.models import AbstractUser
from django.db import models

# INSTALAR UBUNTU
# wsl --install

# INSTALAR REDIS
# curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
# echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
# sudo apt-get update
# sudo apt-get install redis

# INICIAR SERVIDOR REDIS
# wsl -d ubuntu
# sudo service redis-server start
# redis-cli

# INICIAR TRABAJADOR CELERY /AppContenedores/reccsa
# celery -A reccsa worker -l info

#INICIAR CELERY BEAT /AppContenedores/reccsa
# celery -A reccsa beat -l info

# Create your models here.

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

    def __str__(self):
        return f'{self.DocNum} {self.CardName}'
    
