from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from category.forms import CategoriaForm


def categoria(request):

    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categoria/')

    args = {}
    args['form'] = CategoriaForm
    return render(request, 'categoria/index.html', args )
