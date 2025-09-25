# sistemas/models.py
from django.db import models

class Sistema(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Sistema")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Sistema")

    def __str__(self):
        return self.nome

class Atributo(models.Model):
    """Define um atributo que um sistema possui. Ex: Força, Inteligência."""
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name="atributos")
    nome = models.CharField(max_length=50, verbose_name="Nome do Atributo")

    def __str__(self):
        return f"{self.nome} ({self.sistema.nome})"

class Pericia(models.Model):
    """Define uma perícia que um sistema possui. Ex: Atletismo, Furtividade."""
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name="pericias")
    nome = models.CharField(max_length=50, verbose_name="Nome da Perícia")

    def __str__(self):
        return f"{self.nome} ({self.sistema.nome})"

class Habilidade(models.Model):
    """Define uma habilidade que um sistema possui. Ex: Ataque Furtivo, Conjuração ."""
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name="pericias")
    nome = models.CharField(max_length=50, verbose_name="Nome da Perícia")
    descricao = models.TextField(blank=True, verbose_name="Descrição da Habilidade")

    def __str__(self):
        return f"{self.nome} ({self.sistema.nome})"