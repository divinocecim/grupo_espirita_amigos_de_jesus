from django.db import models

# Create your models here.

class Mediuns(models.Model):
    ESTUDO_EVANGELHO_CHOICES = (('S','SIM'),('N','NÃO'))
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    atuante_no_grupo = models.CharField(max_length=1, default='N', choices=ESTUDO_EVANGELHO_CHOICES)
    participa_estudo_evangelho = models.CharField(max_length=1, default='N', choices=ESTUDO_EVANGELHO_CHOICES)
    celphone = models.CharField(max_length=25, blank=True)
 
