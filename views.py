import datetime
from django.shortcuts import render
from .models import Partido

def inicio(request):
    # Obtener los últimos cinco partidos jugados
    ultimos_partidos = Partido.objects.order_by('-fecha_hora').filter(
        fecha_hora__lt=datetime.now())[:5]

    # Obtener los próximos cinco partidos por jugar
    proximos_partidos = Partido.objects.order_by('fecha_hora').filter(
        fecha_hora__gte=datetime.now())[:5]

    return render(request, 'inicio.html', {'ultimos_partidos': ultimos_partidos, 'proximos_partidos': proximos_partidos})