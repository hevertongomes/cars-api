from django.db import models

# Create your models here.

class Marca(models.Model):

    nome = models.CharField('Nome da marca', max_length=250)
    origem = models.CharField('Origem', max_length=250)


class Carro(models.Model):

    nome = models.CharField('Nome do carro', max_length=250)
    km_por_galao = models.IntegerField('Litros por galão')
    cavalo_de_forca = models.IntegerField('Cavalo de força')
    peso = models.IntegerField('Peso')
    aceleracao = models.DecimalField('Acelaracão', max_digits=10, decimal_places=2)
    data_fabricacao = models.DateTimeField('Data de fabricação')
    origem = models.CharField("Origem", max_length=15)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
