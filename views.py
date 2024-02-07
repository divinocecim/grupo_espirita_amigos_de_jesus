from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from .models import Mediuns

def cadastro(request):
    segundas = Mediuns.ESTUDO_EVANGELHO_CHOICES
    #print(segundas)
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'segundas': segundas})
    elif request.method == 'POST':
        username = request.POST.get('celphone')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        participa_estudo_evangelho = request.POST.get('segunda')

        if not senha == confirmar_senha:
            print('Senha e confirmar senha não coincidem...')
            messages.add_message(request, constants.ERROR,'Senha e confirmar senha não coincidem...')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(username=username)

        if user.exists():
            print('Usuário já existe...')
            messages.add_message(request, constants.ERROR,'Usuário já existe...')
            return redirect('/usuarios/cadastro')
        try:
            User.objects.create_user(
                username= username,
                password= senha,
            )       
            mediuns =  Mediuns(
                nome = request.POST.get('username'),
                atuante_no_grupo = 'N',
                participa_estudo_evangelho = request.POST.get('segunda'),
                celphone = request.POST.get('celphone')
            )     
            
            mediuns.save()

            return redirect('/usuarios/logar')

        except:
            messages.add_message(request, constants.ERROR,'Erro interno do servido! Contate o administrador...')
            return redirect('/usuarios/cadastro')
        
        return HttpResponse('Teste')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
    user = auth.authenticate(request, username=username, password=senha)

    if user:
        auth.login(request, user)
        messages.add_message(request, constants.SUCCESS, 'Logado!')
        return redirect('/preces/enviapedido/')
    else:
        messages.add_message(
        request, constants.ERROR, 'Username ou senha inválidos'
        )
        return redirect('/usuarios/logar')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/logar')