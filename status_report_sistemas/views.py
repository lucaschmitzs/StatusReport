from rest_framework import viewsets
from .models import ProjetosEntregas, Gmud, TicketsImpacto
from .serializer import ProjetosEntregasSerializer, GmudSerializer, TicketsImpactoSerializer


class ProjetosEntregasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os projetos e entragas realizados pela equipe de sistemas"""
    queryset = ProjetosEntregas.objects.all()
    serializer_class = ProjetosEntregasSerializer


class GmudViewSet(viewsets.ModelViewSet):
    """Exibindos todas as gmuds abertas e realizadas internamente"""
    queryset = Gmud.objects.all()
    serializer_class = GmudSerializer


class TicketsImpactoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os chamados de grande impacto"""
    queryset = TicketsImpacto.objects.all()
    serializer_class = TicketsImpactoSerializer
