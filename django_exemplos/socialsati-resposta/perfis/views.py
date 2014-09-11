# -*-  coding: utf-8 -*-
#@Author Daniel Michelon De Carli<daniel.de.carli@gmail.com>


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

from models import Perfil, Postagem    

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
                'login2.html',
                {
                    'form':form,
                },
                context_instance=RequestContext(request))




@login_required
def perfil(request, usuario):
    perfil = Perfil.objects.get(usuario__username=usuario)

    postagens_minhas = Postagem.objects.filter(postado_por=request.user).order_by('-id')
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