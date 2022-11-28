from django.forms import *
from core.encuesta.models import Equipos


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
            
            'dispositivo',
            'nombre',
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


