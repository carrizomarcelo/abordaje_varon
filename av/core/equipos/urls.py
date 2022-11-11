from django.urls import path
from core.equipos.views import EquiposListView, EquiposCreateView, EquiposUpdateView, EquiposDeleteView
# , EncuestaFormView

app_name = 'equipos'

urlpatterns = [
    path('list/', EquiposListView.as_view(), name='equipos_list'),
    path('add/', EquiposCreateView.as_view(), name='equipos_add'),
    path('edit/<int:pk>/', EquiposUpdateView.as_view(), name='equipos_edit'),
    path('delete/<int:pk>/', EquiposDeleteView.as_view(), name='equipos_delete'),
    # path('form/', EncuestaFormView.as_view(), name='encuesta_form'),
]