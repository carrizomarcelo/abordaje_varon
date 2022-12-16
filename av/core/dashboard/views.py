from django.views.generic import TemplateView, View
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.encuesta.models import Encuesta
from django.db.models.functions import Coalesce



class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'dashboard.html'
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_graph_encuestas_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range():
        
                total = Encuesta.objects.all()
                data.append(total)
        except:
            pass
        return data


    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de Ingreso'
        contex['graph_encuestas_year_month'] = self.get_graph_encuestas_year_month()
        return contex