from django.shortcuts import render
from django.http import HttpResponse


def relatorios(request):
    return render(request, 'relatorios/index.html')
