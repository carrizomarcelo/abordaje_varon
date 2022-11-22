from av.settings import STATIC_URL
from django.db import models
from datetime import datetime
from django.forms.models import model_to_dict
from av.models import BaseModel
from crum import get_current_user
from multiselectfield import MultiSelectField

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
        verbose_name_plural = 'Opciones'
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
    dpto = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='id_dpto' )
    distrito = models.CharField(max_length=50, verbose_name='Distrito')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'distrito'
        verbose_name = 'Distrito'
        verbose_name_plural = '-distritos'
        ordering = ['id']

class Atencion(models.Model):
    id = models.AutoField(primary_key=True)
    Atencion = models.CharField(max_length=50)
    # nose = models.CharField(max_length=5)
    # otra = models.CharField(max_length=5)

    def __str__(self):
        return str(self.Atencion)

    class Meta:
        db_table = 'atencion'
        verbose_name = 'Atención'
        verbose_name_plural = 'Atención'
        ordering = ['id']

class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', blank=True, null=True)
    direccion = models.CharField(max_length=50, verbose_name='Direccion', blank=True, null=True)
    ubicaciondpto = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento',related_name='dpto_equipos', blank=True, null=True)
    telefono = models.PositiveIntegerField(verbose_name='Telefono', blank=True, null=True)
    tipoatencion = models.ForeignKey(Atencion, on_delete=models.CASCADE, verbose_name='Atención', blank=True, null=True)


    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'equipo'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']


class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad ')

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

class IncumbenciaSeguridad(models.Model):
    id = models.AutoField(primary_key=True)
    incumbencia_seguridad = models.CharField(max_length=50, verbose_name='Ocupacion en la fuerza de seguridad, segun incumbencia')

    def __str__(self):
        return str(self.incumbencia_seguridad)

    class Meta:
        db_table = 'incumbencia_seguridad'
        verbose_name = 'Incumbencia Seguridad'
        verbose_name_plural = 'Incumbencias Seguridad'
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

class SeisMeses(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return str(self.descripcion)

    class Meta:
        db_table = 'tiempo_tratamiento'
        verbose_name = 'Tiempo Tratamiento'
        verbose_name_plural = 'Tiempo Tratamiento'
        ordering = ['id']



class Encuesta(BaseModel):


    TV_PERSONAL = (('Fisica', 'Fisica'),
               ('Violencia Psicologica', 'Violencia Psicologica'),
               ('Violencia Sexual', 'Violencia Sexual'),
               ('Violencia Economica y patrimonial', 'Violencia Economica y patrimonial'),
               ('Violencia Simbolica', 'Violencia Simbolica'),
               ('Violencia Ambiental', 'Violencia Ambiental'))
    TV_FAMILIAR = (('Fisica', 'Fisica'),
               ('Violencia Psicologica', 'Violencia Psicologica'),
               ('Violencia Sexual', 'Violencia Sexual'),
               ('Violencia Economica y patrimonial', 'Violencia Economica y patrimonial'),
               ('Violencia Simbolica', 'Violencia Simbolica'),
               ('Violencia Ambiental', 'Violencia Ambiental'))

    M_PERSONAL = (('Domestica', 'Domestica'),
               ('Institucional', 'Institucional'),
               ('Laboral', 'Laboral'),
               ('Contra la libertad reprodictiva y obstétrica', 'Contra la libertad reprodictiva y obstétrica'),
               ('Mediatica', 'Mediatica'))

    M_FAMILIAR = (('Domestica', 'Domestica'),
               ('Institucional', 'Institucional'),
               ('Laboral', 'Laboral'),
               ('Contra la libertad reprodictiva y obstétrica', 'Contra la libertad reprodictiva y obstétrica'),
               ('Mediatica', 'Mediatica'))


    VG_OTROS = (('Delito Contra la Persona', 'Delito Contra la Persona'),
              ('Delito contra la vida', 'Delito contra la vida'),
              ('Intento de femicidio', 'Intento de femicidio'),
              ('Lesiones Leves', 'Lesiones Leves'),
              ('Lesiones Graves', 'Lesiones Graves'),
              ('Lesiones Gravisimas', 'Lesiones Gravisimas'),
              ('Abuso de Armas (con lesiones)', 'Abuso de Armas (con lesiones)'),
              ('Abuso de Armas (sin lesiones)', 'Abuso de Armas (sin lesiones)'),
              ('Abandono de la persona', 'Abandono de la persona'),
              ('Delitos contra la integridad sexual', 'Delitos contra la integridad sexual'),
              ('Delitos contra la libertad (Amenaza)', ' Delitos contra la libertad (Amenaza)'),
              ('Delitos contra la libertad (Violacion de Domicilio)', ' Delitos contra la libertad (Violacion de Domicilio)'),
              ('Delitos contra la propiedad (Hurto)', ' Delitos contra la propiedad (Hurto)'),
              ('Delitos contra la propiedad (Robo)', ' Delitos contra la propiedad (Robo)'),
              ('Violacion de Domicilio (Extorsión)', ' Violacion de Domicilio (Extorsión)'),
              ('Violacion de Domicilio (Usurpación)', ' Violacion de Domicilio (Usurpación)'),
              ('Violacion de Domicilio (Daños)', ' Violacion de Domicilio (Daños)'),
              ('Violacion de Domicilio (Desobediencia)', ' Violacion de Domicilio (Desobediencia)'))

    AGRESOR = (('Condicion Migratoria', 'Condicion Migratoria'),
              ('Estres Psicosocial', 'Estres Psicosocial'),
              ('Abuso de Sustancias Psicoactivas', 'Abuso de Sustancias Psicoactivas'),
              ('Antecedentes de Violencia en su Biografia', 'Antecedentes de Violencia en su Biografia'),
              ('Tenencia y uso de Armas', 'Tenencia y uso de Armas'),
              ('Antecedentes depresivos', 'Antecedentes depresivos'),
              ('Presencia de miedo o rechazo a los abandonos', 'Presencia de miedo o rechazo a los abandonos'),
              ('Inestabilidad anímica', 'Inestabilidad anímica'),
              ('Egocentrismo', 'Egocentrismo'))

    MUJER = (('Vulnerabilidad Social', 'Vulnerabilidad Social'),
         ('Retractarse de separacion o denuncia al agresor', 'Retractarse de separacion o denuncia al agresor'),
         ('Presencia de hijo no biológico en la convivencia con el agresor', 'Presencia de hijo no biológico en la convivencia con el agresor'))

    SITUACION = (('Relacion en convivencia o matrimonial', 'Relacion en convivencia o matrimonial'),
               ('Solicitud de separacion por parte de la mujer', 'Solicitud de separacion por parte de la mujer'),
               ('ideación de celos del estilo posesivos', 'ideación de celos del estilo posesivos'),
               ('Transitar embarazo', 'Transitar embarazo'),
               ('presedente de conductas de acoso', 'presedente de conductas de acoso'),
               ('conductas de amenazas', 'conductas de amenazas'))

    id = models.AutoField(primary_key=True)
    fechacreacion = models.DateTimeField(default=datetime.now, null=True, verbose_name='Fecha Ficha')
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, verbose_name='Equipo', blank=True, null=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    nro_dni = models.CharField(max_length=11, unique=True, verbose_name='N° DU')
    fecha_nacimiento = models.DateTimeField(default=datetime.now, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, verbose_name='Nacionalidad', null=True, default=9)
    calle = models.CharField(max_length=50, verbose_name='Calle', blank=True, null=True)
    nrocalle = models.PositiveIntegerField(verbose_name='Calle Nro', blank=True, null=True)
    mbt = models.CharField(max_length=50, verbose_name='Mnza/Mblck/Torre', blank=True, null=True)
    pdc = models.CharField(max_length=50, verbose_name='Piso/Casa/Dpto', blank=True, null=True)
    bfpa = models.CharField(max_length=50, verbose_name='Barrio/Finca/Puesto/Asentamiento', blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento', blank=True, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, verbose_name='Distrito', blank=True, null=True)
    telefono = models.PositiveIntegerField(verbose_name='Telefono', blank=True, null=True)
    telefonoa = models.PositiveIntegerField(verbose_name='Telefono Alternativo', blank=True, null=True)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name='Estado Civil', blank=True, null=True)
    ostiene = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='ostiene', verbose_name='Tiene Obra Social', blank=True, null=True)
    osnombre = models.CharField(max_length=50, verbose_name='Nombre de la Obra Social', blank=True, null=True)
    nivel_educacion = models.ForeignKey(Educacion, on_delete=models.CASCADE, verbose_name='Educacion (Maximo Nivel Alcanzado)', blank=True, null=True)
    situacion_laboral = models.ForeignKey(SituacionLaboral, on_delete=models.CASCADE, verbose_name='Situacion Laboral', blank=True, null=True)
    incumbencia_seguridad = models.ForeignKey(IncumbenciaSeguridad, on_delete=models.CASCADE, verbose_name='Ocupación en la fuerza de seguridad, segun incumbencia', blank=True, null=True)
    categoria_ocupacional = models.ForeignKey(CategoriaOcupacional, on_delete=models.CASCADE, verbose_name='Categoria Ocupacional', blank=True, null=True)
    actividad_laboral = models.CharField(max_length=50, verbose_name='Actividad que Realiza', blank=True, null=True)
    domicilio_laboral = models.CharField(max_length=50, verbose_name='Domicilio Laboral', blank=True, null=True)
    
    categoria_inactividad = models.ForeignKey(CategoriaInactividad, on_delete=models.CASCADE, verbose_name='Categoria Inactividad', blank=True, null=True)
    
    miembros_intervinientes = models.ForeignKey(MiembrosConvivientes, on_delete=models.CASCADE, verbose_name='Miembros Convivientes', blank=True, null=True)
    
    ayuda_centroa = models.ForeignKey(CentroAbordaje, on_delete=models.CASCADE, verbose_name='¿Como Llega al Centro de Abordaje?', blank=True, null=True)
    ayduda_centroa_cual = models.CharField(max_length=50, verbose_name='Especificar Cual', blank=True, null=True)
    jfinterviniente = models.CharField(max_length=50, verbose_name='Juzgado/Fiscalía Interviniente', blank=True, null=True)
    obasistencia = models.CharField(max_length=50, verbose_name='Obligatoriedad de Asistencia', blank=True, null=True)
    
    prohibicion_acercamiento = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='prohibicion_acercamiento', verbose_name='Prohibicion de Acercamiento', blank=True, null=True)
    prohibicion_quien = models.CharField(max_length=50, verbose_name='Hacia quien/es', blank=True, null=True)
    pulsera = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='pulsera', verbose_name='Pulsera Electronica', blank=True, null=True)
    acceso_arma =  models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='acceso_arma', verbose_name='¿Tiene Acceso a armas de fuego o similar?', blank=True, null=True)
    
    
    antecedentes_judiciales = models.ForeignKey(Opcion, on_delete=models.CASCADE,related_name='antecedentes_judiciales' ,verbose_name='Antecedentes Judiciales', blank=True, null=True)
    
    antecedentes_otros = MultiSelectField(choices=VG_OTROS, blank=True, null=True)
    
    ddnombre = models.CharField(max_length=50, verbose_name='Nombre/s', blank=True, null=True)
    ddapellido = models.CharField(max_length=50, verbose_name='Apellido/s', blank=True, null=True)
    ddnro_dni = models.CharField(max_length=11, unique=True, verbose_name='N° DU')

    atps_psicologico = models.ForeignKey(Opcion, on_delete=models.CASCADE, verbose_name='Antecedente Psicologico',related_name='psicologico', blank=True, null=True)
    atps_psiquiatrico = models.ForeignKey(Opcion, on_delete=models.CASCADE, verbose_name='Antecedente Psiquiatrico',related_name='psiquiatrico', blank=True, null=True)
    atps_medicacion = models.ForeignKey(Opcion, on_delete=models.CASCADE, verbose_name='Toma Medicación',related_name='medicacion', blank=True, null=True)
    atps_medicacion_nombre = models.CharField(max_length=200, verbose_name='Nombre - Medicación', blank=True, null=True)
    atps_medicacion_vigente = models.ForeignKey(Opcion, on_delete=models.CASCADE,related_name='medicacion_vigente', verbose_name='Medicación vigente', blank=True, null=True)
    atps_psico_psiqui_6_meses = models.ForeignKey(SeisMeses, on_delete=models.CASCADE,related_name='atps_psico_psiqui_6_meses', verbose_name='Tratamiento 6 meses', blank=True, null=True)
    observaciones = models.TextField(verbose_name='OBSERVACIONES', blank=True, null=True)
    ###
    tv_personal = MultiSelectField(max_length=200, max_choices=6, choices=TV_PERSONAL, blank=True, null=True)

    tv_familiar = MultiSelectField(max_length=200, max_choices=6, choices=TV_FAMILIAR, blank=True, null=True)

    modalidad_personal = MultiSelectField(max_length=200, max_choices=6, choices=M_PERSONAL, blank=True, null=True)

    modalidad_familiar = MultiSelectField(max_length=200, max_choices=6, choices=M_FAMILIAR, blank=True, null=True)

    agresor = MultiSelectField(max_length=200, max_choices=6, choices=AGRESOR, blank=True, null=True)

    mujer = MultiSelectField(max_length=200, max_choices=6, choices=MUJER, blank=True, null=True)

    situacion = MultiSelectField(max_length=200, max_choices=6, choices=SITUACION, blank=True, null=True )

    estado = models.BooleanField(default=True)
    
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
