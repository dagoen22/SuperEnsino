"""superensino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from avaliacoes.api.viewsets import *

route = routers.DefaultRouter()

route.register('alternativas/',AlternativasViewSet, basename="alternativas")
route.register('avaliacoes/',AvaliacaoViewSet, basename="avaliacoes")
route.register('exercicios/',ExerciciosViewSet, basename="exercicio")
route.register('respostas/',RespostasViewSet, basename="respostas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avaliacoes.urls')),
    path('', include("django.contrib.auth.urls")),
    path('api/',include(route.urls))
]
