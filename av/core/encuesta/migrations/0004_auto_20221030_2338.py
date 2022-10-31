# Generated by Django 3.2.4 on 2022-10-30 23:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0003_auto_20221028_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='agresor',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Condicion Migratoria'), ('2', 'Estres Psicosocial'), ('3', 'Abuso de Sustancias Psicoactivas'), ('4', 'Antecedentes de Violencia en su Biografia'), ('5', 'Tenencia y uso de Armas'), ('6', 'Antecedentes depresivos'), ('7', 'Presencia de miedo o rechazo a los abandonos'), ('8', 'Inestabilidad anímica'), ('9', 'Egocentrismo')], max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='modalidad_familiar',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Domestica'), (2, 'Institucional'), (3, 'Laboral'), (4, 'Contra la libertad reprodictiva y obstétrica'), (5, 'Mediatica')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='modalidad_personal',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Domestica'), (2, 'Institucional'), (3, 'Laboral'), (4, 'Contra la libertad reprodictiva y obstétrica'), (5, 'Mediatica')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='mujer',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Vulnerabilidad Social'), (2, 'Retractarse de separacion o denuncia al agresor'), (3, 'Presencia de hijo no biológico en la convivencia con el agresor')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='situacion',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Relacion en convivencia o matrimonial'), (2, 'Solicitud de separacion por parte de la mujer'), (3, 'ideación de celos del estilo posesivos'), (4, 'Transitar embarazo'), (5, 'presedente de conductas de acoso'), (6, 'conductas de amenazas')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='tv_familiar',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Fisica'), (2, 'Violencia Psicologica'), (3, 'Violencia Sexual'), (4, 'Violencia Economica y patrimonial'), (5, 'Violencia Simbolica'), (6, 'Violencia Ambiental')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='tv_personal',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Fisica'), (2, 'Violencia Psicologica'), (3, 'Violencia Sexual'), (4, 'Violencia Economica y patrimonial'), (5, 'Violencia Simbolica'), (6, 'Violencia Ambiental')], max_length=11, null=True),
        ),
    ]