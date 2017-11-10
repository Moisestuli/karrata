from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from produtos.forms import ProdutoAdminForm
from encomenda.forms import EncomendaForm
from django.template.context_processors import csrf
from produtos.models import Produto
from category.models import Category
from encomenda.models import Encomenda
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def todos_produtos(request):

    if request.method == 'POST':
        form = ProdutoAdminForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect( '/produto/todos' )

    args = {}
    args.update(csrf(request))
    args['form'] = ProdutoAdminForm
    args['formulario'] = EncomendaForm
    args['user'] = request.user
    args['produtos'] = Produto.objects.all()
    args['categorias'] = Category.objects.all()

    # paginacao
    paginacao = Paginator(args['produtos'], 6)
    page = request.GET.get('page')

    try:
        args['produtos'] = paginacao.page(page)
    except PageNotAnInteger:
        args['produtos'] = paginacao.page(1)
    except EmptyPage:
        args['produtos'] = paginacao.page(paginacao.num_pages)

    args['encomendas']  =  Encomenda.objects.all()

    return render( request, 'produtos/index.html', args )

def vender_produto(request, produto_slug = None):

    return HttpResponse("ver produto")

def produto_single(request, pk = None):

    pk = int(pk)
    args = {}
    args['produto'] = get_object_or_404(Produto, pk=pk)
    p = args['produto']
    args['categories'] = p.categories.filter(is_active=True)
    args['fornecedores'] = p.fornecedores.filter(is_active=True)
    return render(request,"produtos/single.html",args )

def mostra_carrinho(request, pk):

    pk = str(pk)
    produto = get_object_or_404(Produto, pk= pk)


    return HttpResponse("mostra carrino %s" % produto.nome )

def produto_adiciona(request):

    return render(request, 'produtos/vendido.html')
