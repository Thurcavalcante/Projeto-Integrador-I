from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')    

def perfil(request):
    return render(request, 'perfil.html')      