from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from produtos.models import Produto
from vender.models import Vender


def produto_vendido(request):

    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente','')
        produto_id   = request.POST.get('produto_id','')
        valor        = request.POST.get('valor','')
        preco        = request.POST.get('preco','')
        quantidade   = request.POST.get('quantity','')

        # Tudo  produto
        args['produto'] = get_object_or_404(Produto, id=produto_id)
        vender_obj      = Vender()
        p = args['produto']
        proco = p.preco
        quantidade = int(quantidade)
        args['total'] = quantidade * proco
        total         = args['total']

        # vender agora
        vender_obj.nome_cliente = nome_cliente
        vender_obj.quantidade   = +quantidade
        vender_obj.produto = p
        vender_obj.ultimo_pagamento = total
        # extra
        total_comprado = vender_obj.total_comprado()
        # extra
        vender_obj.total_comprado = total_comprado

        # fazer troco
        valor = int(valor)
        troco = vender_obj.ultimo_troco(valor)
        vender_obj.troco = troco
        vender_obj.save()

        """  dados para printar """
        args['nome_cliente'] = nome_cliente
        args['troco'] = troco
        args['quatidade'] = quantidade

        return render(request,'produtos/vendido.html', args)

