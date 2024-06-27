from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    filial = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
