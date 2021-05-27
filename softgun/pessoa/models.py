from django.db import models

# Create your models here.

class pessoa(models.Model):
    cod = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=40)
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=12)
    tipopessoa= models.CharField(max_length=20)

 