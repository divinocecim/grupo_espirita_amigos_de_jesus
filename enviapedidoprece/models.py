from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class PedidoPrece(models.Model):
    ESTADO_ACOLHIDO_CHOICES = (('S','Encarnado'),('N','Desencarnado'))
    id = models.AutoField(primary_key=True)
    id_solicitante = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_pedido = models.DateTimeField()
    nome_acolhido = models.CharField(max_length=100)
    acolhido_encarnado = models.CharField(max_length=1, default='S',choices=ESTADO_ACOLHIDO_CHOICES)
    motivo_prece = models.TextField(null=True)
