from django.shortcuts import render

# Create your views here.


def test(request):
    return render(request, "Agendas/Test.html")


def add(request):
    return render(request, "Agendas/agregar_clientes.html")

