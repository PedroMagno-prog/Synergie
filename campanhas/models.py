# campanhas/models.py
from django.db import models
from sistemas.models import Sistema, Atributo, Pericia

class Ficha(models.Model):
    """A ficha de um personagem."""
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sistema = models.ForeignKey(Sistema, on_delete=models.PROTECT, verbose_name="Sistema de Jogo")

    def __str__(self):
        return self.nome

class ValorAtributoFicha(models.Model):
    """Armazena o valor de um atributo para UMA ficha específica."""
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name="atributos")
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)

    class Meta:
        # Garante que não teremos 'Força' duas vezes na mesma ficha
        unique_together = ('ficha', 'atributo')

    def __str__(self):
        return f"{self.ficha.nome} - {self.atributo.nome}: {self.valor}"

class ValorPericiaFicha(models.Model):
    """Armazena o valor de uma perícia para UMA ficha específica."""
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name="pericias")
    pericia = models.ForeignKey(Pericia, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)

    class Meta:
        unique_together = ('ficha', 'pericia')

    def __str__(self):
        return f"{self.ficha.nome} - {self.pericia.nome}: {self.valor}"