from rest_framework import viewsets
from avaliacoes.api import serializers
from avaliacoes.models import Alternativas, Avaliacoes, Exercicios, Respostas

class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AvaliacoesSerializer
    queryset = Avaliacoes.objects.all()

class RespostasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RespostasSerializer
    queryset = Respostas.objects.all()

class ExerciciosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExerciciosSerializer
    queryset = Exercicios.objects.all()

class AlternativasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlternativasSerializer
    queryset = Alternativas.objects.all()