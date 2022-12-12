
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict
from core.encuesta.models import Equipos
from crum import get_current_request

from av.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    equipo_nombre = models.ForeignKey(Equipos, on_delete=models.CASCADE, verbose_name='Equipo de trabajo', null=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

    


    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.set_password(self.password)
    #     else:
    #         user = User.objects.get(pk=self.pk)
    #         if user.password != self.password:
    #             self.set_password(self.password)
    #     super().save(*args, **kwargs)