from django.shortcuts import render, get_object_or_404, redirect
from produtos.models import Produto
from django.http import HttpResponse
from carts.models import Cart
from cliente.models import Cliente
from relatorios.models import Relatorio


def adiciona_carrinho(request, pk):

    pk = int(pk)
    produto = get_object_or_404(Produto, pk=pk)

    return render(request, 'carrinho/index.html', {'produto': produto})

def processa_carrinho(request):

    cart = Cart()
    r = Relatorio()


    if request.method == 'POST':

        produto = request.POST.get('produto')
        cliente = request.POST.get('cliente')
        preco = request.POST.get('preco')
        pk    = request.POST.get('pk')
        quantidade = request.POST.get('quantidade')
        count      = None
        p = get_object_or_404(Produto, pk=pk)

        if Cliente.objects.filter(nome=cliente).exists():

                # Pega o cliente ja existente
                a  = Cliente.objects.get(nome=cliente)

                # Inseri na tabela Carrinho
                cart.produto = produto
                cart.quantidade = quantidade
                cart.preco = p.preco
                cart.funcionario = request.user.username
                #cart.funcionario = request.user
                cart.cliente = cliente

                # Atribui vezes de compras do cliente
                count = a.compras_realizadas  + 1
                a.compras_realizadas = count

                # Inseri dados na table relatorios
                quantidade   = float(quantidade)
                prc          = float(p.preco)
                total_vendas = prc * quantidade

                r.produto = produto
                r.cliente = cliente
                r.quantidade = quantidade
                r.preco      = p.preco
                r.funcionario = request.user.username
                r.total_vendas = total_vendas

                # Salvamos
                r.save()
                a.save()
                cart.save()

        else:

            test_cli = Cliente()
            test_cli.nome = cliente
            cart.produto = produto
            cart.quantidade = quantidade
            cart.preco = p.preco
            cart.funcionario = request.user.username
            cart.cliente = cliente

            # Inseri dados na table relatorios
            quantidade   = float(quantidade)
            prc          = float(p.preco)
            total_vendas = prc * quantidade

            r.produto = produto
            r.cliente = cliente
            r.quantidade = quantidade
            r.preco      = p.preco
            r.funcionario = request.user.username
            r.total_vendas = total_vendas

            # Salvamos
            r.save()
            test_cli.save()
        cart.save()

        return redirect('/carrinho/ver/')
    return HttpResponse('nada')

def mostra_carrinho(request):

    cart = Cart.objects.all()

    return render(request, 'carrinho/cart.html', {'cart': cart})
