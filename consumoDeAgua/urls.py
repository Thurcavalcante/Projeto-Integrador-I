"""consumoDeAgua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, painel, painel2, autenticacao, desconectar, cadastro_manual, pagina_usuarios, registro, dados
from core.views import listar_alerta, cadastrar_alerta, editar_alerta, remover_alerta
from core.views import listar_consumo, cadastrar_consumo, editar_consumo, remover_consumo
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('cadastro/', cadastro, name='cadastro'),
    path('login/', autenticacao, name='login'), 
    path('logout/', desconectar, name='logout'),
    path('painel/', painel, name='painel'),
    path('painel2/', painel2, name='painel2'), #Adicionado até conseguir autenticar a página pádrão.
    path('cadastro_manual/', cadastro_manual, name='cadastro_manual'),
    path('pagina_usuarios/', pagina_usuarios, name='pagina_usuarios'), 
    path('registro/', registro, name='registro'),
    path('dados/<str:cpf>/', dados, name='dados'), #roda dados, recebendo o parâmetro id do usuário.

    path('alerta/', listar_alerta, name='listar_alerta'),#Aletta
    path('alerta_cadastrar/', cadastrar_alerta, name='cadastrar_alerta'),
    path('alerta_editar/<int:id>/', editar_alerta, name='editar_alerta'),
    path('alerta_remover/<int:id>/', remover_alerta, name='remover_alerta'),

    path('consumo/', listar_consumo, name='listar_consumo'),#Consumo
    path('consumo_cadastrar/', cadastrar_consumo, name='cadastrar_consumo'),
    path('consumo_editar/<int:id>/', editar_consumo, name='editar_consumo'),
    path('consumo_remover/<int:id>/', remover_consumo, name='remover_consumo'),
]


