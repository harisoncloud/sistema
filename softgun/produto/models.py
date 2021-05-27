from django.db import models

# Create your models here.

class produto(models.Model):
    cod = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    especificacoes = models.CharField(max_length=400)
    calibre = models.CharField(max_length=20)
    agrupadorMapa = models.IntegerField()

def __str__(self):
    return self.nome




