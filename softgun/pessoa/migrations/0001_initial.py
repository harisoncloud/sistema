# Generated by Django 3.2.3 on 2021-05-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=40)),
                ('endereco', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=12)),
                ('tipopessoa', models.CharField(max_length=20)),
            ],
        ),
    ]
