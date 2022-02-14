from dataclasses import field
from rest_framework import serializers
from avaliacoes.models import *

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = '__all__'


class RespostasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respostas
        fields = '__all__'


class ExerciciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = '__all__'
    

class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativas
        fields = '__all__'