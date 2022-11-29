from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.reports.forms import ReportForm

# Create your views here.
class ReportEncuestaView(TemplateView):
    template_name = 'encuesta/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte Encuestas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reports:encuesta_report')
        context['form'] = ReportForm()
        return context