from av.settings import STATIC_URL
from django.db import models
from datetime import datetime
from django.forms.models import model_to_dict
from av.models import BaseModel
from crum import get_current_user
# from encuesta.forms import EncuestaForm


# Create your models here.
# from django.forms import model_to_dict
# from abordajev.config.settings import MEDIA_URL, STATIC_URL


class Opcion(models.Model):
    id = models.AutoField(primary_key=True)
    opcion = models.CharField(max_length=5)
    # nose = models.CharField(max_length=5)
    # otra = models.CharField(max_length=5)

    def __str__(self):
        return str(self.opcion)

    class Meta:
        db_table = 'opcion'
        verbose_name = 'Opcion'
        verbose_name_plural = 'opciones'
        ordering = ['id']

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    dpto = models.CharField(max_length=50, verbose_name='Departamento')

    def __str__(self):
        return str(self.dpto)

    class Meta:
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']


class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    dpto = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='id_dpto' )
    distrito = models.CharField(max_length=50, verbose_name='Distrito')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'distrito'
        verbose_name = 'Distrito'
        verbose_name_plural = '-distritos'
        ordering = ['id']

class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad')

    def __str__(self):
        return str(self.nacionalidad)

    def toJSON(self):
        item = model_to_dict(self)
        # item = {'id': self.id, 'nombre': self.nombre}
        return item
    
    class Meta:
        db_table = 'nacionalidad'
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'
        ordering = ['id']



class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=50, verbose_name='Estado CIvil')

    def __str__(self):
        return str(self.estado_civil)

    class Meta:
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'
        ordering = ['id']



class Educacion(models.Model):
    id = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=50, verbose_name='Nivel Educativo (Maximo Alcanzado)')

    def __str__(self):
        return str(self.nivel)

    class Meta:
        db_table = 'nivel_educativo'
        verbose_name = 'Nivel Educativo'
        verbose_name_plural = 'Niveles Educativos'
        ordering = ['id']

class SituacionLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    situacion_laboral = models.CharField(max_length=50, verbose_name='Situacion Laboral')

    def __str__(self):
        return str(self.situacion_laboral)
    class Meta:
        db_table = 'situacion_laboral'
        verbose_name = 'Situacion Laboral'
        verbose_name_plural = 'Situaciones Laborales'
        ordering = ['id']

class CategoriaOcupacional(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_ocupacion = models.CharField(max_length=50, verbose_name='Categoria Ocupacional')

    def __str__(self):
        return str(self.categoria_ocupacion)
    class Meta:
        db_table = 'cat_ocupacional'
        verbose_name = 'Categoria Ocupacional'
        verbose_name_plural = 'Categoria Ocupacional'
        ordering = ['id']


class CategoriaInactividad(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_inactividad = models.CharField(max_length=50, verbose_name='Categoria de Inactividad')

    def __str__(self):
        return str(self.categoria_inactividad)

    class Meta:
        db_table = 'categoria_inactividad'
        verbose_name = 'Categoria de Inactividad'
        verbose_name_plural = 'Categorias de Inactividad'
        ordering = ['id']

class MiembrosConvivientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre:')
    edad = models.CharField(max_length=50, verbose_name='Edad:')
    parentesco = models.CharField(max_length=50, verbose_name='Parentesco:')
    hijos = models.CharField(max_length=50, verbose_name='Hijos - Propios Anteriores de la PSVG')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'miembros_convivientes'
        verbose_name = 'Miembros Convivientes'
        verbose_name_plural = 'Miembros Convivientes'
        ordering = ['id']


class CentroAbordaje(models.Model):
    id = models.AutoField(primary_key=True)
    abordaje_como_llega = models.CharField(max_length=50, verbose_name='¿Como Llega al Centro de Abordaje?')

    def __str__(self):
        return str(self.abordaje_como_llega)

    class Meta:
        db_table = 'centro_abordaje'
        verbose_name = 'Centro de Abordaje'
        verbose_name_plural = 'Centros de Abordaje'
        ordering = ['id']


class Encuesta(BaseModel):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    nro_dni = models.CharField(max_length=11, unique=True, verbose_name='N° DNI')
    fecha_nacimiento = models.DateTimeField(default=datetime.now, null=True)
    edad = models.PositiveIntegerField(verbose_name='Edad', blank=True, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.PROTECT, verbose_name='Nacionalidad', null=True, default=9)
    calle = models.CharField(max_length=50, verbose_name='Calle', blank=True, null=True)
    rocalle = models.PositiveIntegerField(verbose_name='Calle Nro', blank=True, null=True)
    mbt = models.CharField(max_length=50, verbose_name='Mnza/Mblck/Torre', blank=True, null=True)
    pdc = models.CharField(max_length=50, verbose_name='Piso/Casa/Dpto', blank=True, null=True)
    bfpa = models.CharField(max_length=50, verbose_name='Barrio/Finca/Puesto/Asentamiento', blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento', blank=True, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.PROTECT, verbose_name='Distrito', blank=True, null=True)
    telefono = models.PositiveIntegerField(verbose_name='Telefono', blank=True, null=True)
    telefonoa = models.PositiveIntegerField(verbose_name='Telefono Alternativo', blank=True, null=True)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT, verbose_name='Estado Civil', blank=True, null=True)
    ostiene = models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='ostiene', verbose_name='Tiene Obra Social', blank=True, null=True)
    oscual = models.CharField(max_length=50, verbose_name='Nombre de la Obra Social', blank=True, null=True)
    nivel_educacion = models.ForeignKey(Educacion, on_delete=models.PROTECT, verbose_name='Educacion (Maximo Nivel Alcanzado)', blank=True, null=True)
    situacion_laboral = models.ForeignKey(SituacionLaboral, on_delete=models.PROTECT, verbose_name='Situacion Laboral', blank=True, null=True)
    horas_situacionlaboral = models.PositiveIntegerField(verbose_name='Cantidad de Horas que Trabajo por Semana', blank=True, null=True)
    categoria_ocupacional = models.ForeignKey(CategoriaOcupacional, on_delete=models.PROTECT, verbose_name='Categoria Ocupacional', blank=True, null=True)
    actividad_laboral = models.CharField(max_length=50, verbose_name='Actividad que Realiza', blank=True, null=True)
    domicilio_laboral = models.CharField(max_length=50, verbose_name='Domicilio Laboral', blank=True, null=True)
    categoria_inactividad = models.ForeignKey(CategoriaInactividad, on_delete=models.PROTECT, verbose_name='Categoria Inactividad', blank=True, null=True)
    miembros_intervinientes = models.ForeignKey(MiembrosConvivientes, on_delete=models.PROTECT, verbose_name='Miembros Convivientes', blank=True, null=True)
    ayuda_centroa = models.ForeignKey(CentroAbordaje, on_delete=models.PROTECT, verbose_name='¿Como Llega al Centro de Abordaje?', blank=True, null=True)
    ayduda_centroa_cual = models.CharField(max_length=50, verbose_name='Especificar Cual', blank=True, null=True)
    jfinterviniente = models.CharField(max_length=50, verbose_name='Juzgado/Fiscalía Interviniente', blank=True, null=True)
    obasistencia = models.CharField(max_length=50, verbose_name='Obligatoriedad de Asistencia', blank=True, null=True)
    detenido = models.CharField(max_length=50, verbose_name='Detenido', blank=True, null=True)
    prohibicion_acercamiento = models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='prohibicion_acercamiento', verbose_name='Prohibicion de Acercamiento', blank=True, null=True)
    prohibicion_quien = models.CharField(max_length=50, verbose_name='Hacia quien/es', blank=True, null=True)
    pulsera = models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='pulsera', verbose_name='Pulsera Electronica', blank=True, null=True)
    acceso_arma =  models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='acceso_arma', verbose_name='¿Tiene Acceso a armas de fuego o similar?', blank=True, null=True)
    arma_tipo = models.CharField(max_length=50, verbose_name='Tipo de Arma', blank=True, null=True)
    antecedentes_vg = models.CharField(max_length=200, verbose_name='Por VG', blank=True, null=True)
    antecedentes_otros = models.CharField(max_length=200, verbose_name='Otros', blank=True, null=True)
    pddnombre = models.CharField(max_length=50, verbose_name='Nombre Completo', blank=True, null=True)
    pddtelefono = models.PositiveIntegerField(verbose_name='Telefono', blank=True, null=True)
    pdddomicilio_conocido = models.CharField(max_length=200, verbose_name='Domicilo Conocido', blank=True, null=True)
    dpanombre = models.CharField(max_length=50, verbose_name='Nombre Completo', blank=True, null=True)
    dpatelefono = models.PositiveIntegerField(verbose_name='Telefono', blank=True, null=True)
    dpadomicilio_conocido = models.CharField(max_length=50, verbose_name='Nombre Completo', blank=True, null=True)
    apanteriodes = models.CharField(max_length=50, verbose_name='Anteriores', blank=True, null=True)
    apvigentes = models.CharField(max_length=50, verbose_name='Vigentes', blank=True, null=True)
    aptratamiento =  models.ForeignKey(Opcion, on_delete=models.PROTECT, related_name='aptratamiento', verbose_name='Tratamiento Farmacologico', blank=True, null=True)
    aptratamiento_cual = models.CharField(max_length=50, verbose_name='¿Cual?', blank=True, null=True)
    observaciones = models.TextField(verbose_name='OBSERVACIONES', blank=True, null=True)
    equipo = models.CharField(max_length=50, verbose_name='Equipo', blank=True, null=True)
    # fecharegistro = models.DateField(default=datetime.now, null=True)
    fechacreacion = models.DateTimeField(default=datetime.now, null=True, verbose_name='Fecha Ficha')
    # fechaactualiza = models.DateField(auto_now_add=True, null=True)   
    baja = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
        super(Encuesta, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        # item = {'id': self.id, 'nombre': self.nombre}
        return item

    class Meta:
        db_table = 'encuesta'
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'
        ordering = ['id']
