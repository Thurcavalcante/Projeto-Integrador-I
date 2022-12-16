from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100)

class Usuario(AbstractUser):# Vai conter no BD, uma sequecia de colunas padrão + os campos criados abaixo.
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11, unique=True, primary_key=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
    #categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    USERNAME_FIELD = 'cpf' #A partir de agora o usuario deverá logar com o CPF, e não mais com o usuario.

    # CPF: 222
    # Senha: 123

    class Meta: #Definindo permissões que o usuario poderá assumir 
        permissions = [
            ("permissao_adm_1", "podera acessar a view da pagina usuarios.html"),
            ("permissao_adm_2", "podera visualizar o privado do painel.html")
        ]

class Historico_Consumo(models.Model):
    nome = models.CharField("Nome", max_length=100) #Altertar para os campos corretos
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Alerta(models.Model): #Tabela Alerta
     m3 = models.IntegerField('Metros_c') 
     email = models.CharField('Email', max_length=100)
     descricao = models.CharField('Descricao', max_length=200)    

class Consumo(models.Model): #Tabela Consumo
     h_inicial = models.CharField('H_Inicial', max_length=5) #Colunas
     h_final = models.CharField('H_Final', max_length=5)
     dias = models.IntegerField('Dias')     