# Generated by Django 3.2.3 on 2021-05-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('especificacoes', models.CharField(max_length=400)),
                ('calibre', models.CharField(max_length=20)),
                ('agrupadorMapa', models.IntegerField()),
            ],
        ),
    ]