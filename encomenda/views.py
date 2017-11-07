from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from encomenda.models import Encomenda
from encomenda.forms import EncomendaForm

def encomendar(request):

    args = {}

    if request.method == 'POST':
        form = EncomendaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect( '/encomenda/' )

    args['formulario'] = EncomendaForm

    return render(request, 'encomenda/index.html', args)

def encomenda(request, pk):

    args = {}
    args['encomenda'] = get_object_or_404(Encomenda, pk=pk)
    return render(request, 'encomenda/single.html', args)
