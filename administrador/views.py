from django.shortcuts import render
from funcionario.forms import FuncionarioForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from fornecedor.forms import FornecedorForm
from fornecedor.models import Fornecedor
from configuracao.models import Configuracao
# paginacao
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def criafuncionario(request):

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/criar-funcionario/')
    args = {}
    args['users'] = User.objects.all()
    args['perfil'] = Configuracao.objects.all()
    args.update(csrf(request))
    args['form'] = FuncionarioForm

    # paginacao
    paginacao = Paginator(args['users'], 10)
    page      = request.GET.get('page')

    try:
        args['users'] = paginacao.page(page)
    except PageNotAnInteger:
        args['users'] = paginacao.page(1)
    except EmptyPage:
        args['users'] = paginacao.page(paginacao.num_pages)

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
