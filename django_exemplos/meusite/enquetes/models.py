# coding: utf-8 

from django.db import models 

class Enquete(models.Model):
    questao = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField(u'Date de publicação')

class Escolha(models.Model):
    enquete = models.ForeignKey(Enquete)
    texto_da_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)