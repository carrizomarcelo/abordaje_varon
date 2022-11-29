from django.urls import path
from core.reports.views import ReportEncuestaView
# , EncuestaFormView

app_name = 'reports'

urlpatterns = [
    path('encuesta/', ReportEncuestaView.as_view(), name='encuesta_report'),
    
]