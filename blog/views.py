from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.template import loader
from . import models

# Create your views here.
class HolaMundo(TemplateView):
    template_name = "hola-mundo.html"

    def get_context_data(self, **kwargs):
        context = super(HolaMundo, self).get_context_data(**kwargs)

        context['nombre'] = "contraslash"

        return context

class CrearPost(CreateView):
    model = models.Post
    fields = (
        'titulo',
        'cuerpo'
    )
    template_name = "crear.html"
    success_url = "/"

class ListaPost(ListView):
    queryset = models.Post.objects.all()
    template_name = "lista.html"
    context_object_name = "lista"

class DetallePost(DetailView):
    model = models.Post
    template_name = "detalle.html"
    context_object_name = "post"

class ActualizarPost(UpdateView):
    model = models.Post
    fields = (
        'titulo',
        'cuerpo'
    )
    template_name = "actualizar.html"
    success_url = "/"

class EliminarPost(DeleteView):
    model = models.Post
    success_url = "/"
