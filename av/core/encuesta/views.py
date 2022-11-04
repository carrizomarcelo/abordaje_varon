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

from core.encuesta.forms import DdForm, EncuestaForm
from av.mixin import ValidatePermissionRequiredMixin
from core.encuesta.models import *


class EncuestaListView(LoginRequiredMixin, ListView):
    model = Encuesta
    template_name = 'encuesta/encuesta_list.html'

    # @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado'
        context['create_url'] = reverse_lazy('encuesta:encuesta_add')
        context['list_url'] = reverse_lazy('encuesta:encuesta_list')
        # print(reverse_lazy('encuesta:encuesta_list'))
        return context


class EncuestaCreateView(CreateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'encuesta/encuesta_create.html'
    success_url = reverse_lazy('encuesta:encuesta_list')

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
        return JsonResponse(data)
        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Encuesta'
        context['list_url'] = reverse_lazy('encuesta:encuesta_list')
        # context['departamento'] = Departamento.objects.all()
        # context['distrito'] = Distrito.objects.all()
        context['action'] = 'add'
        

        return context


class EncuestaUpdateView(UpdateView):

    model = Encuesta
    form_class = EncuestaForm
    template_name = 'encuesta/encuesta_update.html'
    success_url = reverse_lazy('encuesta:encuesta_list')

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
        context['title'] = 'Editar Encuesta'
        context['list_url'] = reverse_lazy('encuesta:encuesta_list')
        context['action'] = 'edit'
        return context


class EncuestaDeleteView(DeleteView):
    model = Encuesta
    template_name = 'encuesta/encuesta_delete.html'
    success_url = reverse_lazy('encuesta:encuesta_list')

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
        context['title'] = 'Eliminar Encuesta'
        context['list_url'] = reverse_lazy('encuesta:encuesta_list')
        return context


class EncuestaFormView(FormView):
    form_class = EncuestaForm
    template_name = 'encuesta/encuesta_create.html'
    success_url = reverse_lazy('encuesta:encuesta_list')

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
        context['title'] = 'Agregar Encuesta - FORM'
        context['list_url'] = reverse_lazy('encuesta:encuesta_list')
        return context

class DdView(TemplateView):
    template_name = 'dd.html'

    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_distrito_id':
                data = []
                for i in Distrito.objects.filter(dpto=request.POST['id']):
                    data.append({'id': i.id, 'distrito': i.distrito})
            else:
                data['error'] = 'ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | DJANGO'
        context['form'] = DdForm()
        return context