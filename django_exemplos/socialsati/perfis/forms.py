# -*-  coding: utf-8 -*-
#@Author Daniel Michelon De Carli<daniel.de.carli@gmail.com>

from django import forms
from perfis.models import Postagem

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem

        fields = (  
            'conteudo',
        )