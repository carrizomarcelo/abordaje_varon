from django.shortcuts import render
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks.messages import Error
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import is_valid_path
from django.utils.decorators import async_only_middleware, method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  TemplateView, UpdateView)

from core.encuesta.forms import DdForm, EncuestaForm
from core.equipos.forms import EquiposForm
from av.mixin import ValidatePermissionRequiredMixin
from core.encuesta.models import Encuesta

# Create your views here.
class AsistenciaListView(LoginRequiredMixin, ListView):
    model = Encuesta
    template_name = 'asistencia/asistencia_list.html'

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado'
        # context['create_url'] = reverse_lazy('asistencia:asistencia_add')
        # context['list_url'] = reverse_lazy('asistencia:asistencia_list')
        # print(reverse_lazy('encuesta:encuesta_list'))
        return context