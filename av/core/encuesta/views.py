# from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks.messages import Error
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
from core.encuesta.models import *
from django.views import View
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

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
            if action == 'search_distrito_id':
                data = [{'id': '', 'text': '---------'}]
                for i in Distrito.objects.filter(dpto=request.POST['id']):
                    data.append({'id': i.id, 'text': i.distrito})
            elif action == 'add':
                form = self.get_form()
                data = form.save()
                
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        


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
            if action == 'search_distrito_id':
                data = [{'id': '', 'text': '---------'}]
                for i in Distrito.objects.filter(dpto=request.POST['id']):
                    data.append({'id': i.id, 'text': i.distrito})
            elif action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    

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
    form_class = DdForm

    # @method_decorator(csrf_exempt)
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
        context['title'] = ''
        context['list_url'] = reverse_lazy('equipos:equipos_list')
        context['action'] = 'add'
        context['form'] = EquiposForm()
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
        context['form'] = EquiposForm()
        return context


class EncuestaInovicePdfView(View):
    
    def link_callback(self, uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
    
    
    
    
    
    def get(self, request, *args, **kwargs):
        try:   
            template = get_template('encuesta/invoice.html')
            context = {
                'encuesta': Encuesta.objects.get(pk=self.kwargs['pk']),
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/Logotipo_de_la_Provincia_de_Mendoza.png')

            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
                )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('encuesta:encuesta_list'))
