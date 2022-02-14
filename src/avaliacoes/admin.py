from django.contrib import admin

# Register your models here.
from .models import Avaliacoes, Alternativas, Exercicios, Respostas

admin.site.register(Avaliacoes)
admin.site.register(Alternativas)
admin.site.register(Exercicios)
admin.site.register(Respostas)