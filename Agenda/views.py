from django.shortcuts import render
from .models import Evento
# Create your views here.


def test(request):
    return render(request, "Agendas/Index.html")


def add_clients(request):
    return render(request, "Agendas/agregar_clientes.html")


def list_of_events(request):
    events = Evento.objects.order_by('NombreEvento')

    context = {'Eventos': events}

    return render(request, "Agendas/eventos.html", context)


def materiales(request):
    return render(request, "Agendas/materiales.html")

