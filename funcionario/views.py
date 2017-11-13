from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from funcionario.forms import FuncionarioForm
from configuracao.models import Configuracao


def funcionario_eliminar(request, username = None):

    user = User.objects.get(username=username)
    user.delete()

    return HttpResponseRedirect('/admin/criar-funcionario/')

def funcionario_editar(request, pk ):
    if request.method == 'GET':
        pk = int(pk)
        args = {}
        a = get_object_or_404(Configuracao, pk=pk)
        return HttpResponse(a.imagem)

def fornecedor_editar(request):
    return HttpResponse("forncedor")


    """
    args = {}

    args['form'] = FuncionarioForm
    args['funcionario']  = get_object_or_404(User, pk=pk)
    return render(request, 'fornecedor/editar.html', args)
 """
