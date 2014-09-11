# -*-  coding: utf-8 -*-
#@Author Daniel Michelon De Carli<daniel.de.carli@gmail.com>

from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    seguindo = models.ManyToManyField(User, null=True, blank=True, related_name='segue')

    def __unicode__(self):
        return self.usuario.username
        

class Postagem(models.Model):
    postado_por = models.ForeignKey(User)
    conteudo = models.CharField(max_length=140 )
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Conteúdo: %s - postado por: %s"%(self.conteudo, self.postado_por.username)