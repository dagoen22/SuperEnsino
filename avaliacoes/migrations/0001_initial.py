# Generated by Django 4.0.2 on 2022-02-14 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=600)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.avaliacoes')),
            ],
        ),
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.avaliacoes')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.exercicios')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternativa_correta', models.BooleanField()),
                ('descricao', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.exercicios')),
            ],
        ),
    ]