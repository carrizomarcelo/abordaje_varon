# Generated by Django 3.2.4 on 2022-10-31 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0007_auto_20221031_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacionalidad',
            name='nacionalidad',
            field=models.CharField(max_length=50, verbose_name='Nacionalidad '),
        ),
    ]
