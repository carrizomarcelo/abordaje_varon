from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.decorators import async_only_middleware, method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.encuesta.models import Encuesta

from core.reports.forms import ReportForm

# Create your views here.
class ReportEncuestaView(TemplateView):
    template_name = 'encuesta/reports.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Encuesta.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.nombre,
                        s.nro_dni,
                        s.fechacreacion.strftime('%d-%m-%Y'),
                        
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte Encuestas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reports:encuesta_report')
        context['form'] = ReportForm()
        return context