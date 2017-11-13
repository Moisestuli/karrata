from django.contrib.auth.models import User
from fornecedor.models import Fornecedor
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from fornecedor.forms import FornecedorForm
from fornecedor.models import Fornecedor

def adiciona_fornecedor(request):

    if request.method == 'POST':

        nome     = request.POST.get('nome','')
        telefone = request.POST.get('telefone','')
        cidade   = request.POST.get('cidade','')

        f = Fornecedor()
        f.nome = nome
        f.telefone = telefone
        f.cidade = cidade
        f.save()

        return HttpResponseRedirect('/admin/fornecedor/')


    args = {}
    args['fornecedores'] = Fornecedor.objects.all()
    args['form'] = FornecedorForm
    return render(request, 'fornecedor/index.html', args)

def fornecedor_eliminar(request, username):
    f = get_object_or_404(Fornecedor, nome=username)
    f.delete()

    return HttpResponseRedirect('/admin/fornecedor/')


def fornecedor_editar(request, username = None):
    args = {}
    args['fornecedor'] = get_object_or_404(Fornecedor, nome=username)
    return render(request, 'fornecedor/editar.html', args)

def fornecedor_actualizar(request , username ):

    if request.method == 'POST':

        nome_actual     = request.POST.get('nome','')
        telefone_actual = request.POST.get('telefone','')
        cidade_actual   = request.POST.get('cidade','')

        f = get_object_or_404(Fornecedor, nome=username)

        f.nome     = nome_actual
        f.telefone = telefone_actual
        f.cidade   = cidade_actual
        f.save()
        return HttpResponseRedirect('/admin/fornecedor/')

    return HttpResponse("Nao e seguro")

def fornecedor_editar(request, pk):
    args = {}
    args['fornecedor']  = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'fornecedor/editar.html', args)
