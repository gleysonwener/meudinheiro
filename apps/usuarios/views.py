# Aqui se encontra as funções que executam as páginas
from django.shortcuts import render


def inicio(request):
    return render(request, 'base.html', {})
