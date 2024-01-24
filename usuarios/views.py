from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

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
                password= senha
            )             
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
        return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/logar')