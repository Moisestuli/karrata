from django.shortcuts import render
from django.http import HttpResponse
from relatorios.models import Relatorio

def relatorios(request):

    args = {}
    args['relatorios'] = Relatorio.objects.all()

    return render(request, 'relatorios/index.html', args)
