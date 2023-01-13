from dataclasses import fields
from .models import Usuario
from .models import Alerta, Consumo, Residencia, Categoria, Periodo_Consumo_Alerta
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'idade', 'cpf', 'categoria']    

# class UsuarioEdicaoForm(UserCreationForm):
#     class Meta:
#         model = Usuario
#         fields = ['username', 'email', 'nome', 'idade', 'cpf']


class AlertaForm(ModelForm): #Criando o formulario da tabela "Alerta"
    class Meta:
        model = Alerta
        fields = ['m3', 'descricao', 'periodo', 'valor_periodo']

class ConsumoForm(ModelForm): #Criando o formulario da tabela "Alerta"
    class Meta:
        model = Consumo
        fields = ['h_inicial', 'h_final', 'dias']    

class ResidenciaForm(ModelForm):
    class Meta:
        model = Residencia    
        fields = ['estado', 'cidade', 'bairro', 'endereco', 'complemento', 'apelido']   

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']    

class Periodo_Consumo_AlertaForm(ModelForm):    
   class Meta:
        model = Periodo_Consumo_Alerta  
        fields = ['periodo', 'horas']