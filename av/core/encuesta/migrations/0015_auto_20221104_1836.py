# Generated by Django 3.2.4 on 2022-11-04 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0014_auto_20221104_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrito',
            name='dpto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.departamento', verbose_name='id_dpto'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='acceso_arma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acceso_arma', to='encuesta.opcion', verbose_name='¿Tiene Acceso a armas de fuego o similar?'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='antecedentes_judiciales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='antecedentes_judiciales', to='encuesta.opcion', verbose_name='Antecedentes Judiciales'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='atps_medicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicacion', to='encuesta.opcion', verbose_name='Toma Medicación'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='atps_medicacion_vigente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicacion_vigente', to='encuesta.opcion', verbose_name='Medicación vigente'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='atps_psico_psiqui_6_meses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atps_psico_psiqui_6_meses', to='encuesta.seismeses', verbose_name='Tratamiento 6 meses'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='atps_psicologico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psicologico', to='encuesta.opcion', verbose_name='Antecedente Psicologico'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='atps_psiquiatrico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psiquiatrico', to='encuesta.opcion', verbose_name='Antecedente Psiquiatrico'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='ayuda_centroa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.centroabordaje', verbose_name='¿Como Llega al Centro de Abordaje?'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='categoria_inactividad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.categoriainactividad', verbose_name='Categoria Inactividad'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='categoria_ocupacional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.categoriaocupacional', verbose_name='Categoria Ocupacional'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.departamento', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.distrito', verbose_name='Distrito'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='estado_civil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.estadocivil', verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='incumbencia_seguridad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.incumbenciaseguridad', verbose_name='Ocupación en la fuerza de seguridad, segun incumbencia'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='miembros_intervinientes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.miembrosconvivientes', verbose_name='Miembros Convivientes'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='nacionalidad',
            field=models.ForeignKey(default=9, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.nacionalidad', verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='nivel_educacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.educacion', verbose_name='Educacion (Maximo Nivel Alcanzado)'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='ostiene',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ostiene', to='encuesta.opcion', verbose_name='Tiene Obra Social'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='prohibicion_acercamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prohibicion_acercamiento', to='encuesta.opcion', verbose_name='Prohibicion de Acercamiento'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='pulsera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pulsera', to='encuesta.opcion', verbose_name='Pulsera Electronica'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='situacion_laboral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.situacionlaboral', verbose_name='Situacion Laboral'),
        ),
    ]
