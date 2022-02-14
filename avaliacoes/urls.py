from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avaliacao/<int:avaliacao_id>',views.avaliacao, name="avaliacao"),
    path('exercicio/<int:avaliacao_id>/<int:exercicio_id>',views.exercicios, name="exercicio"),
]