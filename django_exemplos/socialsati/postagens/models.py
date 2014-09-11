# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    nome_cidade = models.CharField(max_lenght=32)
    usuario = models.ForeignKey(User)
    seguindo = models.ManyToMany(User)

    def __unicode__(self):
        return self.usuario
