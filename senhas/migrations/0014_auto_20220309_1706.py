# Generated by Django 3.2.10 on 2022-03-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0013_alter_viagem_cnpj_empresa_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem_turismo',
            name='celular',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='telefone',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]