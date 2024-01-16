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
from core.views import home, painel, painel_sessao, painel2, painel3, perfil, autenticacao, desconectar, cadastro_manual, pagina_usuarios, registro, dados
from core.views import listar_alerta, cadastrar_alerta, editar_alerta, remover_alerta
from core.views import listar_consumo, cadastrar_consumo, editar_consumo, remover_consumo
from core.views import listar_residencia, cadastrar_residencia, editar_residencia, remover_residencia
from core.views import listar_categoria, cadastrar_categoria, editar_categoria, remover_categoria
from core.views import listar_periodoalerta, cadastrar_periodoalerta, editar_periodoalerta, remover_periodoalerta
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('cadastro/', cadastro, name='cadastro'),
    path('login/', autenticacao, name='login'), 
    path('logout/', desconectar, name='logout'),
    path('perfil/', perfil, name='perfil'), #Adicionado 16/12/22
    path('painel_sessao/<int:id>', painel_sessao, name='painel_sessao'),
    path('painel/', painel, name='painel'),
    path('painel2/', painel2, name='painel2'),
    path('painel3/', painel3, name='painel3'), #Adicionado 
    path('cadastro_manual/', cadastro_manual, name='cadastro_manual'),
    path('pagina_usuarios/<str:categoria_url>/', pagina_usuarios, name='pagina_usuarios'), 
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

    path('residencia/', listar_residencia, name='listar_residencia'),#Residencia
    path('residencia_cadastrar/', cadastrar_residencia, name='cadastrar_residencia'),
    path('residencia_editar/<int:id>/', editar_residencia, name='editar_residencia'),
    path('residencia_remover/<int:id>/', remover_residencia, name='remover_residencia'),

    path('categoria/', listar_categoria, name='listar_categoria'),#Categoria
    path('categoria_cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    path('categoria_editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categoria_remover/<int:id>/', remover_categoria, name='remover_categoria'),

    path('periodoalerta/', listar_periodoalerta, name='listar_periodoalerta'),#Periodo do alerta
    path('periodoalerta_cadastrar/', cadastrar_periodoalerta, name='cadastrar_periodoalerta'),
    path('periodoalerta_editar/<int:id>/', editar_periodoalerta, name='editar_periodoalerta'),
    path('periodoalerta_remover/<int:id>/', remover_periodoalerta, name='remover_periodoalerta'),
]


