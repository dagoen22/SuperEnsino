from traceback import print_tb
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib import messages

from .models import Alternativas, Avaliacoes, Exercicios, Respostas

# Create your views here.


def index(request):
    avaliacoes = list(Avaliacoes.objects.order_by('-timestamp'))
    avaliacoes = {"avaliacoes": avaliacoes}
    return render(request, 'index.html', avaliacoes)


def get_alternativas(id):
    alternativas = Alternativas.objects.get(id=id)
    return alternativas


def aproveitamento(request):
    user = request.user
    respostas = list(Respostas.objects.filter(aluno=user))
    acertos = list(Respostas.objects.filter(aluno=user, correta=True))
    if not acertos:
        return [0,0,0]
    aproveitamento = round(100 / len(respostas) / len(acertos),2) 
    return [len(respostas), len(acertos), aproveitamento]


@login_required
def avaliacao(request, avaliacao_id):
    aprov = aproveitamento(request)
    exercicios = list(Exercicios.objects.filter(avaliacao=avaliacao_id))
    if not exercicios:
        return HttpResponseNotFound('<h1>Parece que essa avaliação não tem exercicios</h1>')
    alternativas = []

    for exercicio in exercicios:
        alternativas.append(get_alternativas(exercicio.id))

    exercicios = {'exercicios': exercicios,
                  'avaliacao_id': avaliacao_id,
                  'aproveitamento': {
                      'total': aprov[0],
                      'total_acertos': aprov[1],
                      'rendimento': aprov[2]
                  }
                  }

    return render(request, 'avaliacao.html', exercicios)


@login_required
def exercicios(request, avaliacao_id, exercicio_id):
    if verifica_questao(request, exercicio_id):
        messages.add_message(request, messages.INFO,
                             f'Você já fez essa questão!, id {avaliacao_id}')
        return redirect(f"/avaliacao/{avaliacao_id}")
    if request.method == 'POST':
        resposta = verifica_resposta(request.POST.get("alternativa"))
        processa_resultado(request, avaliacao_id, exercicio_id, resposta)
        return redirect(f"/avaliacao/{avaliacao_id}")
    alternativas = list(Alternativas.objects.filter(exercicio=exercicio_id))
    exercicio = Exercicios.objects.get(id=exercicio_id)
    retorno = {
        "alternativas": alternativas,
        "exercicio": exercicio
    }
    return render(request, 'exercicio.html', retorno)


@login_required
def processa_resultado(request, avaliacao_id, exercicio_id, resposta):
    alternativa = request.POST.get("alternativa")
    user = request.user
    resposta = Respostas(aluno=user, correta=resposta,
                         exercicio=Exercicios.objects.get(id=exercicio_id),
                         avaliacao=Avaliacoes.objects.get(id=avaliacao_id))
    resposta.save()


def verifica_resposta(id_resposta):
    resposta = Alternativas.objects.get(id=id_resposta)
    return resposta.alternativa_correta


def verifica_questao(request, exercicio):
    user = request.user
    exercicio = Exercicios.objects.get(id=exercicio)
    resposta = Respostas.objects.filter(aluno=user, exercicio=exercicio)
    return bool(resposta)
