from django.db import models


class Loja(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    preco_min = models.DecimalField(max_digits=10, decimal_places=2)
    preco_max = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo


class EmissaoOrdemServico(models.Model):
    numero_os = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True) 

    
    def __str__(self):
        return self.nome
    
class OrdemServico(models.Model):
    numero_os = models.CharField(max_length=20, primary_key=True, unique=True)  # Número da OS como chave primária
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OS {self.numero_os} - {self.loja} - {self.servico}"