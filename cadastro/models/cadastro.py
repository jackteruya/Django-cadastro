import uuid

from django.db import models


class Cadastro(models.Model):

    class SEXO(models.TextChoices):
        MASCULINO = ('M', 'm')
        FEMININO = ('F', 'f')

    id = models.IntegerField(primary_key=True, editable=False, unique=True, auto_created=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO.choices)
    altura = models.IntegerField()
    peso = models.DecimalField(max_digits=7, decimal_places=1)
    nascimento = models.DateTimeField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nome
