from django.contrib import admin
from .models import ProjetosEntregas, Gmud, TicketsImpacto


class ProjetosEntreguesDisplay(admin.ModelAdmin):
    list_display = ('id', 'projetos_entregas', 'observacoes', 'data_inicio', 'data_fim', 'responsavel')
    list_display_links = ('id', 'projetos_entregas')
    search_fields = ('id', 'projetos_entregas', 'data_inicio', 'data_fim', 'responsavel')
    list_per_page = 20

admin.site.register(ProjetosEntregas, ProjetosEntreguesDisplay)


class GmudDisplay(admin.ModelAdmin):
    list_display = ('id', 'data', 'tipo', 'numero', 'descricao', 'ticket', 'area', 'site', 'solicitante', 'executor', 'status', 'hora_inicio', 'hora_fim')
    list_display_links = ('id', 'ticket')
    search_fields = ('id', 'data', 'ticket', 'site')
    list_per_page = 20

admin.site.register(Gmud, GmudDisplay)
