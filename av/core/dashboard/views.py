from django.template import RequestContext
from django.views.generic import TemplateView, View
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.encuesta.models import Encuesta, Equipos
from core.user.models import User
from django.shortcuts import render
from django.db.models.functions import Coalesce



class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'dashboard.html'
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_graph_encuestas_dpto(self):
        data = []
        try:
            year = datetime.now().year
            for d in range(1,19):
                total = Encuesta.departamento().count()
                data.append(total)
        except:
            pass
        return data
    
        

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de Ingreso'
        contex['get_graph_encuestas_dpto'] = self.get_graph_encuestas_dpto()
        contex['users_count'] = User.objects.all().count()
        contex['encuestas_count'] = Encuesta.objects.all().count()
        contex['equipos_count'] = Equipos.objects.all().count()
        return contex