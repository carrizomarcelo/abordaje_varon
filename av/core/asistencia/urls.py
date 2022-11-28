from django.urls import path
from core.asistencia.views import AsistenciaListView
# AsistenciaCreateView, AsistenciaUpdateView, AsistenciaDeleteView
# , AsistenciaFormView

app_name = 'asistencia'

urlpatterns = [
    path('list/', AsistenciaListView.as_view(), name='asistencia_list'),
    # path('add/', AsistenciaCreateView.as_view(), name='asistencia_add'),
    # path('edit/<int:pk>/', AsistenciaUpdateView.as_view(), name='asistencia_edit'),
    # path('delete/<int:pk>/', AsistenciaDeleteView.as_view(), name='asistencia_delete'),
    # path('form/', AsistenciaFormView.as_view(), name='Asistencia_form'),
]