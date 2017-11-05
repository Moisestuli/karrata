from django.shortcuts import render

def encomendar(request):
    return render(request, 'encomenda/index.html')
