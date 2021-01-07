# Generated by Django 3.1.5 on 2021-01-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gmud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(max_length=10)),
                ('tipo', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('ticket', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('solicitante', models.CharField(max_length=50)),
                ('executor', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('hora_inicio', models.TimeField(max_length=20)),
                ('hora_fim', models.TimeField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetosEntregas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projetos_entregas', models.CharField(max_length=255)),
                ('observacoes', models.TextField(max_length=255)),
                ('data_inicio', models.DateField(max_length=10)),
                ('data_fim', models.DateField(max_length=10)),
                ('responsavel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TicketsImpacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('diagnostico', models.CharField(max_length=255)),
                ('jira', models.CharField(max_length=50)),
                ('data_hora_inicio', models.DateTimeField(max_length=50)),
                ('data_hora_fim', models.DateTimeField(max_length=50)),
                ('solucionador', models.CharField(max_length=50)),
                ('responsavel', models.CharField(max_length=50)),
                ('operacao', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=50)),
            ],
        ),
    ]
