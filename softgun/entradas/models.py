from softgun.pessoa.models import pessoa
from django.db import models

# Create your models here.
class entrada(models.Model):
    cod = models.AutoField(primary_key=True)
    numeronf = models.IntegerField()
    dataemissao = models.DateField()
    dataentrada = models.DateField()
    codfornecedor = models.ForeignKey(pessoa.cod)

