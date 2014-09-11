

##############
#########################      Models
###############################################

# -*-  coding: utf-8 -*-
#@Author Daniel Michelon De Carli<daniel.de.carli@gmail.com>

from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.ForeignKey(User, unique=True)
    
    seguindo = models.ManyToManyField(User, 
                                    null=True,
                                    blank=True, 
                                    related_name='segue')

    def __unicode__(self):
        return self.usuario.username
        

class Postagem(models.Model):
    postado_por = models.ForeignKey(User)
    conteudo = models.CharField(max_length=140 )
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Conteúdo: %s - postado por: %s"%(
                                self.conteudo, 
                                self.postado_por.username
                            )



##############
#########################      Admin
###############################################

# -*-  coding: utf-8 -*-
# @Author Daniel Michelon De Carli<daniel.de.carli@gmail.com>

from django.contrib import admin
from perfis.models import Perfil, Postagem

#Primeira parte
admin.site.register(Perfil)

# Turbinando o Admin
class PostagemAdmin(admin.ModelAdmin):
    model = Postagem
    
    list_display = ( 'conteudo','postado_por', 'data')
    fields = ('conteudo','postado_por')
    ordering  = ('data','conteudo')


admin.site.register(Postagem, PostagemAdmin)



########## Rotas
################    urls.py (no projeto)
#####################################################

from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^/?$','perfis.views.login'),
    url(r'^perfil/(?P<usuario>.*)','perfis.views.perfil'),
    url(r'^logout$','django.contrib.auth.views.logout',{'next_page':'/'}, 
        name='logout'),
    url(r'^postar/?$','perfis.views.postar'),
    url(r'^listar/pessoas/?$','perfis.views.listar_pessoas'),
    url(r'^seguindo/?$','perfis.views.seguindo'),
    url(r'^seguir/(?P<usuario>.*)','perfis.views.seguir_pessoa'),
    url(r'^admin/', include(admin.site.urls)),    
) 

########## IMPORTS
#################### views.py (Parte 1) 
########################################################

# RequestContext -> para as variáveis do contexto (Se o usuário está logado...)
# render_to_response -> renderiza um template HTML como resposta
# redirect -> para redirecionar para outra url
from django.shortcuts import RequestContext, render_to_response, redirect

# Classe que representa o formulário de autenticação
from django.contrib.auth.forms import AuthenticationForm

# No exemplo abaixo foi necessário renomear a função login para não dar conflito 
# com a função declarada neste módulo 
from django.contrib.auth import authenticate, login as login_auth

# É utilizado para não usarmos as os endereços URL no caso de um redirencionamento.
# Isso é uma boa prátiva visto que caso as urls sejam renomeadas o sistema irá continuar
# funcionando. 
from django.core.urlresolvers import reverse

# É utilizado para verificar se o usuário está logado
from django.contrib.auth.decorators import login_required

# usado para lista as pessoas da rede social
from django.contrib.auth.models import User

########## login
#################### views.py (Parte 2) 
########################################################


def  login(request):
    # formulário de autenticação
    form = AuthenticationForm(request)
    
    if request.method == 'POST' :
        # pega os dados da submissão do formulário
        username = request.POST['username']
        password = request.POST['password']

        #Esse metodo retorna o usuário caso o username e o password batam
        user = authenticate(username=username,password=password)
        
        if user is not None:

            #Verifica se o usuário está ativo
            if user.is_active :
                #registra o login do usuário no sistema
                login_auth(request, user)
                perfil = None


                try:
                    #tenta pegar o perfil do usuário
                    # Caso o perfil não seja encontrado o django
                    # irá lançar um exceção
                    perfil = Perfil.objects.get(usuario=request.user)
                except:
                    # Caso não exista o perfil é necessário cria-lo
                    # vamos crirar ele no tratamento da exceção
                    perfil = Perfil()
                    perfil.usuario = request.user
                    perfil.save()

                return redirect(reverse('perfis.views.perfil',
                                        kwargs={'usuario':perfil.usuario}))
     

    return render_to_response(
                'login.html',
                {
                    'form':form,
                },
                context_instance=RequestContext(request))

#### Arquivo de configuração da url
url(r'^/?$','perfis.views.login'),

#### Sair
url(r'^logout$','django.contrib.auth.views.logout',{'next_page':'/'}, 
        name='logout'),

########
## login.html
########

{% extends 'base.html' %}

{% block conteudo %}

<div class='container'>
    <div class='row'>
        <div class='span12'>
            <center>
                <form method='post' action=''>
                    {% csrf_token %}
                    {{form}}
                    <br>
                    <button type='submit' class='btn btn-primary'> Logar </button>
                </form>
            </center>
        </div>
    </div>
</div>

{% endblock %}


#######
## Base.html
#######

Mostrar e explicar


########## perfil
#################### views.py (Parte 2) 
########################################################

@login_required
def perfil(request, usuario):
    perfil = Perfil.objects.get(usuario__username=usuario)

    postagens_minhas = Postagem.objects.filter(postado_por=perfil.usuario).order_by('-id')
    postagens_amigos = Postagem.objects.filter(postado_por__in=perfil.seguindo.all()).order_by('-id')

    nome_do_usuario = usuario

    return render_to_response(
        'perfil.html',
        {
            'postagens_minhas': postagens_minhas,
            'postagens_amigos' : postagens_amigos,
            'perfil': perfil
        },
        context_instance=RequestContext(request)
        )

#### Arquivo de configuração da url
url(r'^perfil/(?P<usuario>.*)','perfis.views.perfil'),
   

########
## perfil.html
########



{% extends 'base.html' %}

{% block conteudo %}

<div class='container'>
    <div class='row'>
        <div class='span12'>
            <h1>{{ perfil.usuario.username }}</h1>

             {% if not user.username == perfil.usuario.username %}
                <a class='btn btn-primary' href="{% url 'perfis.views.seguir_pessoa' usuario.username %}">
                 Seguir perfil
                </a>
            {% endif %}
            <hr>
        </div>
    </div>

    <div class='row'>
        <div class='span6'>
            <h3>Postagens amigos</h3>

            {% if postagens_amigos %}
                {% for postagem in postagens_amigos %}
                <div class='well'>
                    {{ postagem.conteudo }}
                    <!--
                    <hr>
                    {{ postagem.data }}
                    -->
                </div>
                <br>
                {% endfor %}
            {% else %}
                Sem postagens
            {% endif %}
        </div>
        <div class='span6'>
            <h3>Minhas postagens</h3>

            {% if postagens_minhas %}
                {% for postagem in postagens_minhas %}
                <div class='well'>
                    {{ postagem.conteudo }}
                    <!--
                    <hr>
                    {{ postagem.data }}
                    -->
                </div>
                <br>
                {% endfor %}
              {% else %}
                Sem postagens
            {% endif %}
        </div>

    </div>
</div>

{% endblock %}


########## postar
#################### views.py (Parte 3) 
########################################################

@login_required
def postar(request):
    from perfis.forms import PostagemForm

    form = PostagemForm(request.POST or None)

    if form.is_valid():
        postagem = form.instance
        postagem.postado_por = request.user
        postagem.save()

        return redirect(reverse('perfis.views.perfil',
                                kwargs={'usuario':request.user}))
     


    return render_to_response(
            'postar.html',
            {'form': form},
            context_instance=RequestContext(request)
        )

#### Arquivo forms.py
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



####
## postar.html
####

{% extends 'base.html' %}

{% block conteudo %}

<div class='container'>
    <div class='row'>
        <div class='span12'>
            <center>
                <form method='POST' action=''>
                    {% csrf_token %}
                    {{ form }}
                    <br>
                    <button type='submit' class='btn btn-primary'>Postar</button>
                </form>
            </center>

        </div>
    </div>
</div>
{% endblock %}

### Configuração da url
url(r'^postar/?$','perfis.views.postar'),
    

########## listar pessoas
#################### views.py (Parte 4) 
########################################################

@login_required
def listar_pessoas(request):
    usuarios = User.objects.filter(is_active=True)

    return render_to_response(
        'listar_pessoas.html',
        {
            'usuarios': usuarios
        },
        context_instance=RequestContext(request)
        )


####
## listar_pessoas.html
####

{% extends 'base.html' %}

{% block conteudo %}

<div class='container'>
    <div class='row'>
        <div class='span12'>
            <h1>Usuários da rede</h1>
            {% if usuarios%}
                <table class='table'>
                    {% for usuario  in usuarios %}
                    <tr>    
                        <td>
                            {{ usuario.username }}
                        </td>
                        <td>
                            {{ usuario.fist_name }}
                        </td>

                        <td>
                            {{ usuario.last_name }}
                        </td>
                        <td>
                            <a class='btn' href="{% url 'perfis.views.perfil' usuario.username %}">
                                Ver perfil
                            </a>
                            {% if not user.username == usuario.username %}
                            <a class='btn btn-primary' href="{% url 'perfis.views.seguir_pessoa' usuario.username %}">
                                Seguir perfil
                            </a>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </table>
            {% else %}
                No momento você não está seguindo ninguém.
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}

########## Seguir pessoa
#################### views.py (Parte 5) 
########################################################

@login_required
def seguir_pessoa(request, usuario):
    perfil = Perfil.objects.get(usuario=request.user)

    seguir = User.objects.get(username=usuario)

    perfil.seguindo.add(seguir)

    seguindo = perfil.seguindo.all()

    return render_to_response(
        'seguindo.html',
        {
            'seguindo': seguindo,
        },
        context_instance=RequestContext(request)
        )

### Configuração da URL
url(r'^seguir/(?P<usuario>.*)','perfis.views.seguir_pessoa'),
    
########## Seguindo
#################### views.py (Parte 6) 
########################################################

@login_required
def seguindo(request):
    perfil = Perfil.objects.get(usuario=request.user)
    seguindo = perfil.seguindo.all()

    return render_to_response(
        'seguindo.html',
        {
            'seguindo': seguindo,
        },
        context_instance=RequestContext(request)
        )


### Configuração da URL
url(r'^seguindo/?$','perfis.views.seguindo'),
   

####
## listar_pessoas.html
####

{% extends 'base.html' %}

{% block conteudo %}

<div class='container'>
    <div class='row'>
        <div class='span12'>
            <h1>Seguindo</h1>
            {% if seguindo %}
                <table class='table'>
                    {% for usuario  in seguindo %}
                    <tr>    
                        <td>
                            {{ usuario.username }}
                        </td>
                        <td>
                            {{ usuario.fist_name }}
                        </td>

                        <td>
                            {{ usuario.last_name }}
                        </td>
                        <td>
                            <a class='btn' href="{% url 'perfis.views.perfil' usuario.username %}">
                                Ver perfil
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </table>
            {% else %}
                No momento você não está seguindo ninguém.
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}





