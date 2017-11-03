from django.shortcuts import render
from funcionario.forms import FuncionarioForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from fornecedor.forms import FornecedorForm
from fornecedor.models import Fornecedor




def criafuncionario(request):

    user = User.objects.all()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/criar-funcionario/')
    args = {}
    args.update(csrf(request))
    args['form'] = FuncionarioForm
    args['users'] = user

    return render(request, 'funcionario.html', args)

def criaforncedor(request):
    user = User.objects.all()

    if request.method == 'POST':
        form = FornecedorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/criarfornecedor/')
    args = {}
    args.update(csrf(request))
    args['form'] = FornecedorForm
    args['users'] = user
    args['fornecedores'] = Fornecedor.objects.all()

    return render(request, 'fornecedor/index.html', args)

def configuracao(request):
    return render(request, 'sistema/configuracao.html')

def analise_dados(request):
    return render(request, 'sistema/analise.html')
