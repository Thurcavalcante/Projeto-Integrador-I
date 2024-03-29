from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    
    def __str__(self):
      return self.nome


class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11, unique=True, primary_key=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    USERNAME_FIELD = 'cpf' 

    class Meta:  
        permissions = [
            ("permissao_adm_1", "podera acessar a view da pagina usuarios.html"),
            ("permissao_adm_2", "podera visualizar o privado do painel.html"),
            ("permissao_adm_3", "podera acessar o Crud categorias e Periodo_Consumo_Alerta")
        ]

class Periodo_Consumo_Alerta(models.Model):
    periodo = models.CharField("Periodo", max_length=100)
    horas = models.IntegerField("Horas do Período")
    def __str__(self):
      return self.periodo

class Residencia(models.Model):      
    complemento = models.CharField('Complemento', max_length=200)   
    apelido = models.CharField('Apelido', max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    cidade = models.CharField('Cidade', max_length=200)  
    estado = models.CharField('Estado', max_length=200)  
    bairro = models.CharField('Bairro', max_length=200)  
    endereco = models.CharField('Endereco', max_length=200)  

class Alerta(models.Model): #Tabela Alerta
    m3 = models.DecimalField("Metros_c", max_digits = 6, decimal_places = 3)
    descricao = models.CharField('Descricao', max_length=200)  
    residencia = models.ForeignKey(Residencia, on_delete=models.PROTECT) 
    periodo = models.ForeignKey(Periodo_Consumo_Alerta, on_delete=models.PROTECT)
    valor_periodo = models.IntegerField("Quantidade do Período")

class Consumo(models.Model): #Tabela Gerencia Consumo
     h_inicial = models.TimeField('H_Inicial')
     h_final = models.TimeField('H_Final')
     dias = models.IntegerField('Dias')  
     residencia = models.ForeignKey(Residencia, on_delete=models.PROTECT) 

class Historico_Consumo(models.Model):
   datahora = models.DateTimeField("Data_Hora") 
   m3 = models.DecimalField("Metros_c", max_digits = 5, decimal_places = 4)
   residencia = models.ForeignKey(Residencia, on_delete=models.PROTECT)

class Vazamento(models.Model): #Hostorico de vazamento
    datahora = models.DateTimeField("Data_Hora")    
    observacao = models.CharField("Observacao", max_length=200)
    consumo = models.ForeignKey(Consumo, on_delete=models.PROTECT)
    residencia = models.ForeignKey(Residencia, on_delete=models.PROTECT)

class Historico_Tarifa(models.Model):
    valor = models.DecimalField("Valor_Tarifa", max_digits = 5, decimal_places = 2)    
    mes = models.DateTimeField("Mes_Consumo")
    historico_consumo = models.ForeignKey(Historico_Consumo, on_delete=models.PROTECT)
    residencia = models.ForeignKey(Residencia, on_delete=models.PROTECT)
    #VARIAÇÕES DE CONSUMO -> 0 a 10m3 = 40,00 de 10 a 12 = 50 -- FALTA INSERIR
  