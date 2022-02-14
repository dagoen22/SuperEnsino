from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Avaliacoes(models.Model):
    titulo = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Exercicios(models.Model):
    descricao = models.CharField(max_length=300)
    avaliacao = models.ForeignKey(Avaliacoes, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

class Alternativas(models.Model):
    exercicio = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
    alternativa_correta = models.BooleanField()
    descricao = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao


class Respostas(models.Model):
    aluno = models.ForeignKey(User,on_delete=models.CASCADE)
    correta = models.BooleanField()
    exercicio = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacoes, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

