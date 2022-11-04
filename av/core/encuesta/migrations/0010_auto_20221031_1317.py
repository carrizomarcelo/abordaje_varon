# Generated by Django 3.2.4 on 2022-10-31 13:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0009_alter_encuesta_antecedentes_otros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='agresor',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Condicion Migratoria'), ('2', 'Estres Psicosocial'), ('3', 'Abuso de Sustancias Psicoactivas'), ('4', 'Antecedentes de Violencia en su Biografia'), ('5', 'Tenencia y uso de Armas'), ('6', 'Antecedentes depresivos'), ('7', 'Presencia de miedo o rechazo a los abandonos'), ('8', 'Inestabilidad anímica'), ('9', 'Egocentrismo')], max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='antecedentes_otros',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Delito Contra la Persona'), ('2', 'Delito contra la vida'), ('3', 'Intento de femicidio'), ('4', 'Lesiones Leves'), ('5', 'Lesiones Graves'), ('6', 'Lesiones Gravisimas'), ('7', 'Abuso de Armas (con lesiones)'), ('8', 'Abuso de Armas (sin lesiones)'), ('9', 'Abandono de la persona'), ('10', 'Delitos contra la integridad sexual'), ('11', ' Delitos contra la libertad (Amenaza)'), ('12', ' Delitos contra la libertad (Violacion de Domicilio)'), ('13', ' Delitos contra la propiedad (Hurto)'), ('14', ' Delitos contra la propiedad (Robo)'), ('15', ' Violacion de Domicilio (Extorsión)'), ('16', ' Violacion de Domicilio (Usurpación)'), ('17', ' Violacion de Domicilio (Daños)'), ('18', ' Violacion de Domicilio (Desobediencia)')], max_length=44, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='modalidad_familiar',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Domestica'), ('2', 'Institucional'), ('3', 'Laboral'), ('4', 'Contra la libertad reprodictiva y obstétrica'), ('5', 'Mediatica')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='modalidad_personal',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Domestica'), ('2', 'Institucional'), ('3', 'Laboral'), ('4', 'Contra la libertad reprodictiva y obstétrica'), ('5', 'Mediatica')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='mujer',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Vulnerabilidad Social'), ('2', 'Retractarse de separacion o denuncia al agresor'), ('3', 'Presencia de hijo no biológico en la convivencia con el agresor')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='situacion',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Relacion en convivencia o matrimonial'), ('2', 'Solicitud de separacion por parte de la mujer'), ('3', 'ideación de celos del estilo posesivos'), ('4', 'Transitar embarazo'), ('5', 'presedente de conductas de acoso'), ('6', 'conductas de amenazas')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='tv_familiar',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Fisica'), ('2', 'Violencia Psicologica'), ('3', 'Violencia Sexual'), ('4', 'Violencia Economica y patrimonial'), ('5', 'Violencia Simbolica'), ('6', 'Violencia Ambiental')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='tv_personal',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Fisica'), ('2', 'Violencia Psicologica'), ('3', 'Violencia Sexual'), ('4', 'Violencia Economica y patrimonial'), ('5', 'Violencia Simbolica'), ('6', 'Violencia Ambiental')], max_length=11, null=True),
        ),
    ]