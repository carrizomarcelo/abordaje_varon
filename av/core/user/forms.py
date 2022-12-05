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
from core.user.models import User
from multiselectfield import MultiSelectField



class UserForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['first_name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined']
        widgets = {

            'equipo': Select(attrs={
                            'placeholder': 'Seleccione...'
                        }),

            'first_name': TextInput(attrs={
                            'placeholder': 'Ingrese nombre/s'
                        }),

            'lastname': TextInput(attrs={
                'placeholder': 'Ingrese apellido/s'
            }),

            'email': EmailField(attrs={
                    'placeholder': 'Ingrese dirección de correo ',
                }),

            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre de usuario',
                }),

            'password': PasswordInput(attrs={
                'placeholder': 'Ingrese su contraseña'
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
 