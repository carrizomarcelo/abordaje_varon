# from django.db.models.fields.files import ImageFieldFile
# from django.contrib.admin.widgets import AutocompleteSelect
# from django.contrib import admin
from django.forms import *
from core.user.models import User


class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = User
        fields = [
            'equipo',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
     ]
        widgets = {

            'equipo': Select(attrs={}),

            'first_name': TextInput(attrs={}),
            
            'last_name': TextInput(attrs={}),
            
            
            'email': EmailInput(attrs={}),
            
            'username': TextInput(attrs={}),
            
            'password': PasswordInput(render_value = True, attrs={}),

        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staf']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
 
    
