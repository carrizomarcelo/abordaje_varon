# Generated by Django 3.2.4 on 2022-10-31 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0005_auto_20221031_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='ddnro_dni',
            field=models.CharField(max_length=11, unique=True, verbose_name='N° DU'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='nro_dni',
            field=models.CharField(max_length=11, unique=True, verbose_name='N° DU'),
        ),
    ]