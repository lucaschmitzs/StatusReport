from django.db import models


class ProjetosEntregas(models.Model):
    objects = models.Manager()
    projetos_entregas = models.CharField(max_length=255, blank=False, null=False)
    observacoes = models.TextField(max_length=255, blank=False, null=False)
    data_inicio = models.DateField(max_length=10, blank=False, null=False)
    data_fim = models.DateField(max_length=10, blank=False, null=False)
    responsavel = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.projetos_entregas


class Gmud(models.Model):
    objects = models.Manager()
    data = models.DateField(max_length=10, blank=False, null=False)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    numero = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=False, null=False)
    ticket = models.CharField(max_length=50, blank=False, null=False)
    area = models.CharField(max_length=100, blank=False, null=False)
    site = models.CharField(max_length=100, blank=False, null=False)
    solicitante = models.CharField(max_length=50, blank=False, null=False)
    executor = models.CharField(max_length=50, blank=False, null=False)
    status = models.CharField(max_length=255, blank=False, null=False)
    hora_inicio = models.TimeField(max_length=20, blank=False, null=False)
    hora_fim = models.TimeField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.descricao


class TicketsImpacto(models.Model):
    objects = models.Manager()
    descricao = models.CharField(max_length=255, blank=False, null=False)
    diagnostico = models.CharField(max_length=255, blank=False, null=False)
    jira = models.CharField(max_length=50, blank=False, null=False)
    data_hora_inicio = models.DateTimeField(max_length=50, blank=False, null=False)
    data_hora_fim = models.DateTimeField(max_length=50, blank=False, null=False)
    solucionador = models.CharField(max_length=50, blank=False, null=False)
    responsavel = models.CharField(max_length=50, blank=False, null=False)
    operacao = models.CharField(max_length=100, blank=False, null=False)
    site = models.CharField(max_length=50, blank=False, null=False)  # SITES = (('', '')) choices=SITES

    def __str__(self):
        return self.descricao
