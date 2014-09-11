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