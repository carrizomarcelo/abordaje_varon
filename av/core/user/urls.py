from django.urls import path
from core.user.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserChangeGroup
# , EncuestaFormView

app_name = 'user'

urlpatterns = [
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('change/group/<int:pk>/', UserChangeGroup.as_view(), name='user_change_group'),
    # path('form/', EncuestaFormView.as_view(), name='encuesta_form'),
]