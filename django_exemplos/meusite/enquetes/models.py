# coding: utf-8 

import datetime
from django.utils import timezone
from django.db import models 

class Enquete(models.Model):
    questao = models.CharField(max_length=200)
    data_de_publicacao = models.DateTimeField(u'Date de publicação')

    def foi_publicado_recentemente(self):
        return self.data_de_publicacao >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.questao


class Escolha(models.Model):
    enquete = models.ForeignKey(Enquete)
    texto_da_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.texto_da_escolha