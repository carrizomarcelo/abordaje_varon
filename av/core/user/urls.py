from django.urls import path
from core.user.views import UserListView, UserCreateView
# AsistenciaCreateView, AsistenciaUpdateView, AsistenciaDeleteView
# , AsistenciaFormView

app_name = 'user'

urlpatterns = [
    path('list/', UserListView.as_view(), name='list_user'),
    path('add/', UserCreateView.as_view(), name='user_add'),
    # path('edit/<int:pk>/', AsistenciaUpdateView.as_view(), name='asistencia_edit'),
    # path('delete/<int:pk>/', AsistenciaDeleteView.as_view(), name='asistencia_delete'),
    # path('form/', AsistenciaFormView.as_view(), name='Asistencia_form'),
    ]