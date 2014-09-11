# coding: utf-8
from django.shortcuts import RequestContext, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_auth
from models import Perfil    

def  login(request):
    mensagem = None
    form = AuthenticationForm(request)
    
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            if user.is_active :
                login_auth(request, user)

                try:
                    perfil = Perfil.objects.get(user=request.user)
                except:
                    perfil = Perfil()
                    perfil.usuario = request.user
                    perfil.save()

                #return redirect(reverse('chamadas.views.painel_geral'))
            else:
                mensagem =  u'Usuário inativo.'
        
    else:
        mensagem = u'Usuário ou senha não confere.'

    return render_to_response(
                'login2.html',
                {
                    'form':form,
                    'mensagem':mensagem
                },
                context_instance=RequestContext(request))



def perfil(request):
    return render_to_response(
        'perfil.html',
        {},


        )


def postar(request):
    return render_to_response(
        'postar.html',
        {},
        

        )