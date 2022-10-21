# from django.db.models.fields.files import ImageFieldFile
# from django.contrib.admin.widgets import AutocompleteSelect
# from django.contrib import admin
from datetime import date
from multiprocessing.sharedctypes import Value
from optparse import Option
from select import select
from xmlrpc.client import DateTime
from django.forms import *
from pandas import options
from core.encuesta.models import *


class EncuestaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            # self.fields['nacionalidad'].widget.attrs.update({'class': 'select2'})
            # self.fields['departamento'].widget.attrs.update({'class': 'select2'})
            # self.fields['distrito'].widget.attrs.update({'class': 'select2'})
            # self.fields['estado_civil'].widget.attrs.update({'class': 'select2'})
            # self.fields['ostiene'].widget.attrs.update({'class': 'select2'})
            # self.fields['nivel_educacion'].widget.attrs.update({'class': 'select2'})
            # self.fields['situacion_laboral'].widget.attrs.update({'class': 'select2'})
            # self.fields['categoria_ocupacional'].widget.attrs.update({'class': 'select2'})
            # self.fields['categoria_inactividad'].widget.attrs.update({'class': 'select2'})
            # self.fields['ayuda_centroa'].widget.attrs.update({'class': 'select2'})
            # self.fields['prohibicion_acercamiento'].widget.attrs.update({'class': 'select2'})
            # self.fields['pulsera'].widget.attrs.update({'class': 'select2'})
            # self.fields['aptratamiento'].widget.attrs.update({'class': 'select2'})
            # self.fields['acceso_arma'].widget.attrs.update({'class': 'select2'})
            self.fields['nombre'].widget.attrs['autofocus'] = True
    departamento = ModelChoiceField(
        queryset=Departamento.objects.all(), widget=Select(attrs={}))
    distrito = ModelChoiceField(
        queryset=Distrito.objects.all(), widget=Select(attrs={}))

    class Meta:
        model = Encuesta
        fields = [
            'nombre',
            'apellido',
            'nro_dni',
            'fecha_nacimiento',
            # 'edad',
            'nacionalidad',
            'departamento',
            'distrito',
            'calle',
            'rocalle',
            'mbt',
            'pdc',
            'bfpa',
            'telefono',
            'telefonoa',
            'estado_civil',
            'ostiene',
            'oscual',
            'nivel_educacion',
            'situacion_laboral',
            'horas_situacionlaboral',
            'categoria_ocupacional',
            'actividad_laboral',
            'domicilio_laboral',
            'categoria_inactividad',
            'miembros_intervinientes',
            'ayuda_centroa',
            'ayduda_centroa_cual',
            'jfinterviniente',
            'obasistencia',
            'detenido',
            'prohibicion_acercamiento',
            'prohibicion_quien',
            'pulsera',
            'acceso_arma',
            'arma_tipo',
            'antecedentes_vg',
            'antecedentes_otros',
            'pddnombre',
            'pddtelefono',
            'pdddomicilio_conocido',
            'dpanombre',
            'dpatelefono',
            'dpadomicilio_conocido',
            'apanteriodes',
            'apvigentes',
            'aptratamiento',
            'aptratamiento_cual',
            'observaciones',
            'equipo',
            'fechacreacion',
        ]
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'apellido': TextInput(attrs={
                'placeholder': 'Ingrese Apellido/s'
            }),

            'nro_dni': NumberInput(attrs={
                'placeholder': 'Ingrese el Nro de DNI'
            }),

            'fecha_nacimiento': DateInput(
                                       attrs={
                                        
                                       }),

            # 'edad': NumberInput(attrs={
            #     'placeholder': 'Ingrese Edad'
            # }),

            'nacionalidad': Select(attrs={
                'placeholder': '',

            }),

            'calle': TextInput(attrs={
                'placeholder': 'Nombre de la Calle'
            }),

            'rocalle': NumberInput(attrs={
                'placeholder': 'Sin Nro, elija el numero 0'
            }),

            'mbt': TextInput(attrs={
                'placeholder': 'Manzana - Monoblock - Torre'
            }),

            'pdc': TextInput(attrs={
                'placeholder': 'Ingrese...'
            }),

            'bfpa': TextInput(attrs={
                'placeholder': 'Ingrese...'
            }),

            'departamento': Select(attrs={
                'placeholder': ''
            }),

            'distrito': Select(attrs={
                'placeholder': ''
            }),

            'telefono': NumberInput(attrs={
                'placeholder': ''
            }),

            'telefonoa': NumberInput(attrs={
                'placeholder': ''
            }),

            # 'estado_civil': Select(attrs={
            #     'placeholder': ''
            # }),

            'ostiene': Select(attrs={
                'placeholder': ''
            }),

            'oscual': TextInput(attrs={
                'placeholder': 'Nombre de la Obras social que posee'
            }),

            # 'nivel_educacion': Select(attrs={
            #     'placeholder': ''
            # }),

            # 'situacion_laboral': Select(attrs={
            #     'placeholder': ''
            # }),

            'horas_situacionlaboral': NumberInput(attrs={
                'placeholder': 'Ingrese la cantidad de horas Semanales'
            }),

            # 'categoria_ocupacional': Select(attrs={
            #     'placeholder': ''
            # }),

            'actividad_laboral': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'domicilio_laboral': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            # 'categoria_inactividad': Select(attrs={
            #     'placeholder': ''
            # }),

            'miembros_intervinientes': TextInput(attrs={
                'placeholder': ''
            }),

            # 'ayuda_centroa': Select(attrs={
            #     'placeholder': ''
            # }),

            'ayduda_centroa_cual': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'jfinterviniente': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'obasistencia': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'detenido': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            # 'prohibicion_acercamiento': Select(attrs={
            #     'placeholder': ''
            # }),

            'prohibicion_quien': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            # 'pulsera': Select(attrs={
            #     'placeholder': ''
            # }),

            'acceso_arma': Select(attrs={
                'placeholder': '...Completar'
            }),

            'arma_tipo': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'antecedentes_vg': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'antecedentes_otros': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'pddnombre': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'pddtelefono': NumberInput(attrs={
                'placeholder': '...Completar'
            }),

            'pdddomicilio_conocido': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'dpanombre': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'dpatelefono': NumberInput(attrs={
                'placeholder': '...Completar'
            }),

            'dpadomicilio_conocido': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'apanteriodes': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'apvigentes': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            # 'aptratamiento': TextInput(attrs={
            #     'placeholder': ''
            # }),

            'aptratamiento_cual': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'observaciones': Textarea(attrs={
                'placeholder': 'Escriba Aquí, el detalle de las observaciones realizadas',
                'rows': "3",
                'cols': "40"
            }),

            'equipo': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'fechacreacion': DateInput(format='%d/%m/%Y',
                                       attrs={
                                           'value': datetime.now().strftime('%d/%m/%Y')
                                       }),




        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class DdForm(Form):
    departamento = ModelChoiceField(queryset=Departamento.objects.all(), widget=Select(attrs={
        'class': 'form-control select2'
    }))

    distrito = ModelChoiceField(queryset=Distrito.objects.none(), widget=Select(attrs={
        'class': 'form-control select2'
    }))

    def clean(self):
        cleaned = super().clean()
        if len(cleaned['nombre']) <= 3:
            raise forms.ValidationError('Escriba al menos 3 Caracteres')
            # self.add_error('nombre', 'Demaciados caracteres')
        return cleaned
