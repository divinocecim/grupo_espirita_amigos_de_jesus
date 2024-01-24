from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PedidoPrece
from datetime import datetime
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def enviapedido(request):
    print('iniciei...')
    print(request.method)
    if request.method == "GET":
        estados = PedidoPrece.ESTADO_ACOLHIDO_CHOICES
         
        pedidoprece = PedidoPrece.objects.filter(id_solicitante=request.user)

        estado_filtrar = request.GET.get('estado')
       
        if estado_filtrar:
            pedidoprece = pedidoprece.filter(acolhido_encarnado=estado_filtrar) 

 
        return render(
            request,
            'novo_pedido_prece.html',
            {
                'estados': estados,
                'pedidospreces': pedidoprece,
            }
            
        )
    elif request.method == 'POST':

        id_solicitante=request.user
        nome_acolhido = request.POST.get('acolhido')
        motivo_prece = request.POST.get('motivo')
        acolhido_encarnado = request.POST.get('estado')
        data_pedido = datetime.now()
        print(f'Solicitante: {id_solicitante}, Acolhido: {nome_acolhido}, Motivo: {motivo_prece}, Encarnado: {acolhido_encarnado}, Data Pedido: {data_pedido}')
      
        print(type(nome_acolhido))
        if len(nome_acolhido) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                'Preencha o Nome do Acolhido com pelo menos 3 letras...',
            )
            return redirect('/preces/enviapedido')

        pedidoprece = PedidoPrece(
            id_solicitante=request.user,
            nome_acolhido=nome_acolhido,
            motivo_prece=motivo_prece,
            acolhido_encarnado=acolhido_encarnado,
            data_pedido = datetime.now()
        )

        pedidoprece.save()

        messages.add_message(
            request, constants.SUCCESS, 'Pedido de prece envidado com sucesso'
        )
        return redirect('/preces/enviapedido')