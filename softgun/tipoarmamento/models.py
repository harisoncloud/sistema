from django.db import models

# Create your models here.

class tipoarmamento(models.Model):
    cod = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, null=False)

