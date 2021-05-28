from django.db import models
# Create your models here.

class entradas(models.Model):
    cod = models.AutoField(primary_key=True)
    numeronf = models.IntegerField
    dataemissao = models.DateField
    dataentrada = models.DateField
    codfornecedor = models.IntegerField

