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
from multiselectfield import MultiSelectField



class EquiposForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['ubicaciondpto'].widget.attrs.update({'class': 'select2'})
            self.fields['nombre'].widget.attrs['autofocus'] = True
        
        
            
    
    class Meta:
        model = Equipos
        fields = [
            'nombre',
            'dispositivo',
            'sigla',
            'direccion',
            'ubicaciondpto',
            'telefono',
            'tipoatencion'  
        ]
        widgets = {


            'nombre': TextInput(attrs={
                            'placeholder': 'Nombre del Equipo de Trabajo'
                        }),

            'dispositivo': Select(attrs={
                'placeholder': 'Seleccione...'
            }),

            'sigla': TextInput(
                attrs={
                    'placeholder': 'Siglas...',
                }),

            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'ubicaciondpto': Select(attrs={
                'placeholder': 'Seleccione...'
            }),

            'tipo': Select(attrs={
                'placeholder': 'Seleccione...'
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

class EncuestaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['nacionalidad'].widget.attrs.update({'class': 'select2'})
            self.fields['departamento'].widget.attrs.update({'class': 'select2'})
            self.fields['distrito'].widget.attrs.update({'class': 'select2'})
            # self.fields['distrito'].widget.attrs['autocomplete'] = True
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
            self.fields['fechacreacion'].widget.attrs['autofocus'] = True
            # self.fields['distrito'].queryset = Distrito.objects.none()

            # if 'departamento' in self.data:
            #     try:
            #         departamento_id = int(self.data.get('departamento'))
            #         self.fields['distrito'].queryset = Distrito.objects.filter(departamento_id).order_by('distrito')
            #     except (ValueError, TypeError):
            #         pass
            # elif self.instance.pk:
            #     self.fields['distrito'].queryset = self.instance.departamento.distrito_set.order_by('distrito')
    # departamento = ModelChoiceField(queryset=Departamento.objects.all())
    # distrito = ModelChoiceField(queryset=Distrito.objects.none())

    # departamento = ModelChoiceField(queryset=Departamento.objects.all(), widget=Select(attrs={
    #     'class': 'form-control select2'
    # }))

    # distrito = ModelChoiceField(queryset=Distrito.objects.none(), widget=Select(attrs={
    #     'class': 'form-control select2'
    # }))

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['nombre']) <= 3:
    #         raise forms.ValidationError('Escriba al menos 3 Caracteres')
    #         # self.add_error('nombre', 'Demaciados caracteres')
    #     return cleaned

    class Meta:
        model = Encuesta
        fields = [
            'fechacreacion',
            'equipo',
            'nombre',
            'apellido',
            'nro_dni',
            'fecha_nacimiento',
            'nacionalidad',
            'calle',
            'nrocalle',
            'mbt',
            'pdc',
            'bfpa',
            'departamento',
            'distrito',          
            'telefono',
            'telefonoa',
            'estado_civil',
            'ostiene',
            'osnombre',
            'nivel_educacion',
            'situacion_laboral',
            'incumbencia_seguridad',
            'categoria_ocupacional',
            'actividad_laboral',
            'domicilio_laboral',
            'miembros_intervinientes',
            'ayuda_centroa',
            'ayduda_centroa_cual',
            'jfinterviniente',
            'obasistencia',
            'prohibicion_acercamiento',
            'prohibicion_quien',
            'pulsera',
            'acceso_arma',
            'antecedentes_judiciales',
            'antecedentes_otros',

            'ddnombre',
            'ddapellido',
            'ddnro_dni',
            'atps_psicologico',
            'atps_psiquiatrico',
            'atps_medicacion',
            'atps_medicacion_nombre',
            'atps_medicacion_vigente',
            'atps_psico_psiqui_6_meses',
            'observaciones',
            'tv_personal',
            'tv_familiar',
            'modalidad_personal',
            'modalidad_familiar',
            'agresor',
            'mujer',
            'situacion',
            'mc_nombre',
            'mc_apellido',
            'mc_fechanacimiento',
            'parentesco',
            'mc_nombre1',
            'mc_apellido1',
            'mc_fechanacimiento1',
            'parentesco1',
            'mc_nombre2',
            'mc_apellido2',
            'mc_fechanacimiento2',
            'parentesco2',
            'mc_nombre3',
            'mc_apellido3',
            'mc_fechanacimiento3',
            'parentesco3'
            
        ]
        widgets = {

            'parentesco': Select(attrs={
                                        'placeholder': '...'
                                    }),
            'parentesco1': Select(attrs={
                                        'placeholder': '...'
                                    }),
            'parentesco2': Select(attrs={
                                        'placeholder': '...'
                                    }),
            'parentesco3': Select(attrs={
                                        'placeholder': '...'
                                    }),

            'mc_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_nombre1': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_nombre2': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),
            
            'mc_nombre3': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_apellido1': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_apellido2': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_apellido3': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'mc_fechanacimiento': DateInput(
                                       attrs={
                                        
                                       }),

            'mc_fechanacimiento1': DateInput(
                                       attrs={
                                        
                                       }),
            
            'mc_fechanacimiento2': DateInput(
                                       attrs={
                                        
                                       }),

            'mc_fechanacimiento3': DateInput(
                                       attrs={
                                        
                                       }),
            
            


            'fechacreacion': DateInput(format='%d/%m/%Y',
                                       attrs={
                                           'value': datetime.now().strftime('%d/%m/%Y')
                                       }),

            'equipo': Select(attrs={
                            'placeholder': '...Completar'
                        }),

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre/s',
                }),

            'apellido': TextInput(attrs={
                'placeholder': 'Ingrese Apellido/s'
            }),

            'nro_dni': NumberInput(attrs={
                'placeholder': 'Ingrese el Nro del DU'
            }),

            'fecha_nacimiento': DateInput(
                                       attrs={
                                        
                                       }),


            'nacionalidad': Select(attrs={
                'placeholder': '',

            }),

            'calle': TextInput(attrs={
                'placeholder': 'Nombre de la Calle'
            }),

            'nrocalle': NumberInput(attrs={
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

            'estado_civil': Select(attrs={
                'placeholder': ''
            }),

            'ostiene': Select(attrs={
                'placeholder': ''
            }),

            'osnombre': TextInput(attrs={
                'placeholder': 'Nombre de la Obras social que posee'
            }),

            'nivel_educacion': Select(attrs={
                'placeholder': ''
            }),

            'situacion_laboral': Select(attrs={
                'placeholder': ''
            }),

            'incumbencia_seguridad': Select(attrs={
                'placeholder': ''
            }),
            
            'categoria_ocupacional': Select(attrs={
                'placeholder': ''
            }),
          
            'actividad_laboral': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'domicilio_laboral': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'categoria_inactividad': Select(attrs={
                'placeholder': ''
            }),

            'miembros_intervinientes': TextInput(attrs={
                'placeholder': ''
            }),

            'ayuda_centroa': Select(attrs={
                'placeholder': ''
            }),

            'ayduda_centroa_cual': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'jfinterviniente': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'obasistencia': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'prohibicion_acercamiento': Select(attrs={
                'placeholder': ''
            }),

            'prohibicion_quien': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'pulsera': Select(attrs={
                'placeholder': ''
            }),

            'acceso_arma': Select(attrs={
                'placeholder': '...Completar'
            }),


            'antecedentes_judiciales': Select(attrs={
                
            }),

            # 'antecedentes_otros': TextInput(attrs={

            # }),

            'ddnombre': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'ddapellido': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'ddnro_dni': TextInput(attrs={
                'placeholder': '...Completar'
            }),

            'atps_psicologico': Select(attrs={
                'placeholder': '...Completar'
            }),

            'atps_psiquiatrico': Select(attrs={
                'placeholder': '...Completar'
            }),
        
            'atps_medicacion': Select(attrs={
                'placeholder': '...Completar'
            }),
    
            'atps_medicacion_nombre': TextInput(attrs={
                'placeholder': '...Completar'
            }),
    
            'atps_medicacion_vigente': Select(attrs={
                'placeholder': '...Completar'
            }),

            'atps_psico_psiqui_6_meses': Select(attrs={

            }),

            'observaciones': Textarea(attrs={
                'placeholder': 'Escriba Aqu??, el detalle de las observaciones realizadas',
                'rows': "3",
                'cols': "40"
            }),
    
    
            'tv_personal': CheckboxInput(attrs={
                
            }),

            'tv_familiar': CheckboxSelectMultiple(attrs={
                
            }),

            'modalidad_personal': CheckboxSelectMultiple(attrs={
                
            }),

            'modalidad_familiar': CheckboxSelectMultiple(attrs={
                
            }),

            'agresor': CheckboxSelectMultiple(attrs={
                
            }),

            'mujer': CheckboxSelectMultiple(attrs={
                
            }),

            'situacion': CheckboxSelectMultiple(attrs={
                
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


