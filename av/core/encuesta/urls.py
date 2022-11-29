from django.urls import path
from core.encuesta.views import EncuestaListView, EncuestaCreateView, EncuestaUpdateView, EncuestaDeleteView, EncuestaInovicePdfView
# , EncuestaFormView

app_name = 'encuesta'

urlpatterns = [
    path('list/', EncuestaListView.as_view(), name='encuesta_list'),
    path('add/', EncuestaCreateView.as_view(), name='encuesta_add'),
    path('edit/<int:pk>/', EncuestaUpdateView.as_view(), name='encuesta_edit'),
    path('delete/<int:pk>/', EncuestaDeleteView.as_view(), name='encuesta_delete'),
    path('invoice/<int:pk>/', EncuestaInovicePdfView.as_view(), name='encuesta_invoice_pdf'),
    # path('form/', EncuestaFormView.as_view(), name='encuesta_form'),
]