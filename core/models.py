from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11, unique=True, primary_key=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
   # categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    USERNAME_FIELD = 'cpf' 

    class Meta:  
        permissions = [
            ("permissao_adm_1", "podera acessar a view da pagina usuarios.html"),
            ("permissao_adm_2", "podera visualizar o privado do painel.html")
        ]

class Historico_Consumo(models.Model):
    nome = models.CharField("Nome", max_length=100) #Alterar para os campos corretos
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Alerta(models.Model): #Tabela Alerta
    m3 = models.IntegerField('Metros_c') 
 #   tempo_cons = models.CharField('Tempo_cons', max_length=50) #ERRO, TEVE QUE TIRAR DE FORMS E CADASTRAR_ALERTA.HTML
    descricao = models.CharField('Descricao', max_length=200)    

class Consumo(models.Model): #Tabela Consumo
     h_inicial = models.TimeField('H_Inicial') #Colunas
     h_final = models.TimeField('H_Final')
     dias = models.IntegerField('Dias')  


class Residencia(models.Model):      
    endereco = models.CharField('Endereco', max_length=200)   
    apelido = models.CharField('Apelido', max_length=50)