from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect


def home_page(request):

    if request.user.is_authenticated():
        return render(request, 'sistema/index.html', dict(user=request.user))
    else:
        return render(request, 'contas/login.html')

def logar(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if request.method == 'POST':
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Algo correu mal ou senha ou nome nao exoste")

def logout(request):

    auth.logout(request)

    return HttpResponseRedirect('/')
