# Generated by Django 5.0.1 on 2024-01-24 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoPrece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_pedido', models.DateTimeField()),
                ('nome_acolhido', models.CharField(max_length=100)),
                ('acolhido_encarnado', models.CharField(choices=[('S', 'Encarnado'), ('N', 'Desencarnado')], max_length=1)),
                ('motivo_prece', models.TextField(null=True)),
                ('id_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
