from rest_framework import serializers
from .models import	ProjetosEntregas, Gmud, TicketsImpacto


class ProjetosEntregasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetosEntregas
        fields = '__all__'


class GmudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gmud
        fields = '__all__'


class TicketsImpactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsImpacto
        fields = '__all__'
