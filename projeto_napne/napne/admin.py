from django.contrib import admin
from .models import Categoria, Solicitacao


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criada_em')
    search_fields = ('nome',)


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'nome_completo', 'matricula', 'categoria', 'urgencia', 'status', 'criada_em')
    list_filter = ('status', 'urgencia', 'categoria', 'campus')
    search_fields = ('nome_completo', 'matricula', 'assunto', 'email')
