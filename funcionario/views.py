from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def funcionario_eliminar(request, username = None):

    user = User.objects.get(username=username)
    user.delete()

    return HttpResponseRedirect('/admin/criar-funcionario/')

def funcionario_editar(request, username = None):

    f = get_object_or_404(User, username=username)

    args = {}
    args['funcionario'] = f
    return render(request, 'funcionario/editar.html', args)
