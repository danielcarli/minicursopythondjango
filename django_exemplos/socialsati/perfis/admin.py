from django.contrib import admin
from perfis.models import Perfil

admin.site.register(Perfil)


class PostagemAdmin(admin.ModelAdmin):
    model = Postagem
    
    list_display = ( 'conteudo','postado_por', 'data')
    fields = ('conteudo','postado_por')
    ordering  = ('data','conteudo')


admin.site.register(Postagem, PostagemAdmin)
