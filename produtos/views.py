from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from produtos.forms import ProdutoAdminForm
from django.template.context_processors import csrf
from produtos.models import Produto
from carrinho.cart import Cart

def todos_produtos(request):

    if request.method == 'POST':
        form = ProdutoAdminForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect( '/produto/todos' )

    args = {}
    args.update(csrf(request))
    args['form'] = ProdutoAdminForm
    args['user'] = request.user
    args['produtos'] = Produto.objects.all()

    return render( request, 'produtos/index.html', args )

def vender_produto(request, produto_slug = None):

    produto = get_object_or_404(Produto, slug=produto_slug)
    cart = Cart(request)
    cart.add(produto, produto.preco)
    return render(request, 'produtos/single.html', dict(cart=Cart(request)))

def produto_single(request, produto_slug = None):

    args = {}
    args.update(csrf(request))
    #args['form'] = VendaAdminForm
    args['produtos'] = Produto.objects.all()
    args['produto'] = get_object_or_404(Produto, slug=produto_slug)
    p = args['produto']
    args['categories'] = p.categories.filter(is_active=True)
    args['fornecedores'] = p.fornecedores.filter(is_active=True)
    args['cart']         = Cart(request)

    return render(request, 'produtos/single.html', args)

def mostra_carrinho(request):
    return HttpResponse("mostra carrino")

def produto_adiciona(request):

    return render(request, 'produtos/vendido.html')
