from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from produtos.models import Produto
from carrinho.cart import Cart


def carrinho_add(request):

    if request.method == 'POST':

        produto_id = request.POST.get('produto_id','')
        quantidade  = request.POST.get('quantity','')
        valor       = request.POST.get('valor','')
        produto    = get_object_or_404(Produto, pk=produto_id)
        cart       = Cart(request)
        if quantidade == '':
            return HttpResponse("quantidade nao pode ser nulo")
        else:
            cart.add(produto, produto.preco, quantidade, valor)
        return render(request, 'carrinho/cart.html', dict(cart=Cart(request)))

    if not request.method == 'POST':
        return render(request, 'carrinho/cart.html', dict(cart=Cart(request)))

def carrinho_remover(request, product_id):
    product = get_object_or_404(Produto, pk=product_id)
    cart    = Cart(request)
    cart.remove(product)

    return HttpResponseRedirect('/carrinho/carrinho', dict(cart=Cart(request)))

def carrinho_comprar(request):
    return HttpResponse("Ok vamos comprar")
