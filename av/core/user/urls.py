from django.urls import path
from core.user.views import UserListView, UserCreateView #, UserUpdateView, UserDeleteView
# , EncuestaFormView

app_name = 'user'

urlpatterns = [
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    # path('edit/<int:pk>/', EquiposUpdateView.as_view(), name='equipos_edit'),
    # path('delete/<int:pk>/', EquiposDeleteView.as_view(), name='equipos_delete'),
    # path('form/', EncuestaFormView.as_view(), name='encuesta_form'),
]