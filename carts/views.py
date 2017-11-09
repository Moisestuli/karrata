from django.shortcuts import render, get_object_or_404, redirect
from produtos.models import Produto
from django.http import HttpResponse
from carts.models import Cart
from cliente.models import Cliente
from decimal import Decimal

def adiciona_carrinho(request, pk):

    pk = int(pk)
    produto = get_object_or_404(Produto, pk=pk)

    return render(request, 'carrinho/index.html', {'produto': produto})

def processa_carrinho(request):

    cart = Cart()


    if request.method == 'POST':

        produto = request.POST.get('produto')
        cliente = request.POST.get('cliente')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        count      = None
        price = Decimal(preco)

        if Cliente.objects.filter(nome=cliente).exists():
                a  = Cliente.objects.get(nome=cliente)
                cart.produto = produto
                cart.quantidade = quantidade
                cart.preco = preco
                #cart.funcionario = request.user
                cart.cliente = cliente
                count = a.compras_realizadas  + 1
                a.compras_realizadas = count
                a.save()
                cart.save()

        else:

            test_cli = Cliente()
            test_cli.nome = cliente
            cart.produto = produto
            cart.quantidade = quantidade
            cart.preco = preco
            #cart.funcionario = request.username
            cart.cliente = cliente
            test_cli.save()
        cart.save()

        return redirect('/carrinho/ver/')
    return HttpResponse('nada')

def mostra_carrinho(request):

    cart = Cart.objects.all()

    return render(request, 'carrinho/cart.html', {'cart': cart})
