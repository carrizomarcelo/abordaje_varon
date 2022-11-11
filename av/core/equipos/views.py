# from django.contrib.auth.decorators import login_required
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
from core.encuesta.models import Equipos


from core.equipos.forms import EquiposForm
from av.mixin import ValidatePermissionRequiredMixin



class EquiposListView(LoginRequiredMixin, ListView):
    model = Equipos
    template_name = 'equipos/equipos_list.html'

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado'
        context['create_url'] = reverse_lazy('equipos:equipos_add')
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        return context


class EquiposCreateView(CreateView):
    model = Equipos
    form_class = EquiposForm
    template_name = 'equipos/equipos_create.html'
    success_url = reverse_lazy('equipos:equipos_list')

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        data = {}
        
        try:
            action = request.POST['action']
            
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar equipo'
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        context['action'] = 'add'
        return context


class EquiposUpdateView(UpdateView):

    model = Equipos
    form_class = EquiposForm
    template_name = 'equipos/equipos_update.html'
    success_url = reverse_lazy('equipos:equipos_list')

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']                    
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Equipo'
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        context['action'] = 'edit'
        return context


class EquiposDeleteView(DeleteView):
    model = Equipos
    template_name = 'equipos/equipos_delete.html'
    success_url = reverse_lazy('equipos:equipos_list')

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Equipo'
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        return context


class EquiposFormView(FormView):
    form_class = EquiposForm
    template_name = 'equipos/equipos_create.html'
    success_url = reverse_lazy('equipos:equipos_list')


    def form_valid(self, form):
        print(form.is_valid)
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid)
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Equipo - FORM'
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        return context