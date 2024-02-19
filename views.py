import datetime
from django.shortcuts import render
from .models import Partido
from django.views import generic

import models


def inicio(request):
    # Obtener los últimos cinco partidos jugados
    ultimos_partidos = Partido.objects.order_by('-fecha_hora').filter(
        fecha_hora__lt=datetime.now())[:5]

    # Obtener los próximos cinco partidos por jugar
    proximos_partidos = Partido.objects.order_by('fecha_hora').filter(
        fecha_hora__gte=datetime.now())[:5]

    return render(request, 'inicio.html', {'ultimos_partidos': ultimos_partidos, 'proximos_partidos': proximos_partidos})

def deportes(request):
    deportes=models.Deporte.objects.all()
    contexto={}
    contexto['deportes']=deportes
    return render(request,"deportes.html",contexto)

def instalaciones(request):
    instalaciones=models.Instalacion.objects.all()
    contexto={}
    contexto['instalaciones']=instalaciones
    return render(request,"instalaciones.html",contexto)

class DeportesListView(generic.ListView):
    model=models.Deporte
    template_name = "deportes.html"

class DeporteCreateView(generic.CreateView):
    model = models.Deporte
    fields = []
    template_name = 'create.html'
    success_url = "/inicio/deporte/"

class DeporteUpdateView(generic.UpdateView):
    model = models.Deporte
    fields = []
    template_name = 'update.html'
    success_url = "/inicio/deporte/"

class DeporteDeleteView(generic.DeleteView):
    model = models.Deporte
    fields = []
    template_name = 'delete.html'
    success_url = "/inicio/deporte/"

class InstalacionesListView(generic.ListView):
    model = models.Instalacion
    template_name = 'instalaciones.html'

class InstalacionCreateView(generic.CreateView):
    model = models.Instalacion
    template_name = 'create.html'
    fields = []
    success_url = "/inicio/instalacion/"

class InstalacionUpdateView(generic.UpdateView):
    model = models.Instalacion
    template_name = 'update.html'
    fields = []
    success_url = "/inicio/instalacion/"

class InstalacionDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'delete.html'
    fields = []
    success_url = "/inicio/instalacion/"

class EquiposListView(generic.ListView):
    model = models.Equipo
    template_name = 'equipos.html'
    success_url = "/inicio/equipo/"

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'equipo_detalle.html'
    success_url = "/inicio/equipo/"

class EquipoCreateView(generic.CreateView):
    model = models.Equipo
    fields = ['nombre', 'deporte', 'contacto', 'telefono', 'email']
    template_name = 'create.html'
    success_url = "/inicio/equipo/"

class EquipoUpdateView(generic.UpdateView):
    model = models.Equipo
    fields = ['nombre', 'deporte', 'contacto', 'telefono', 'email']
    template_name = 'update.html'
    success_url = "/inicio/equipo/"

class EquipoDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'delete.html'
    success_url = "/inicio/equipo/"

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    fields = ['nombre', 'apellido1', 'apellido2', 'dorsal', 'fecha_nacimiento', 'altura', 'peso', 'telefono']
    template_name = 'create.html'
    success_url = 'inicio/equipo/'  # Ajusta esta URL según tu estructura de URL