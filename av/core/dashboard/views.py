from itertools import count
from django.views.generic import TemplateView
from datetime import datetime

from core.encuesta.models import Encuesta
from django.db.models.functions import Coalesce


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_graph_encuestas_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1,13):
        
                total = Encuesta.objects.filter(fechacreacion__year=year, fechacreacion__month=m)
                data.append(total)
        except:
            pass
        return data


    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['panel'] = 'Panel de Ingreso'
        contex['graph_encuestas_year_month'] = self.get_graph_encuestas_year_month()
        return contex