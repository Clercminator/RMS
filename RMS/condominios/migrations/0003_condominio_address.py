# Generated by Django 5.0 on 2023-12-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0002_rename_bancos_banco_rename_condominios_condominio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
