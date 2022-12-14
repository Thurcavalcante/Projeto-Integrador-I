from dataclasses import fields
from .models import Usuario
from .models import Alerta, Consumo
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'idade', 'cpf']    


class AlertaForm(ModelForm): #Criando o formulario da tabela "Alerta"
    class Meta:
        model = Alerta
        fields = ['m3', 'email', 'descricao']

class ConsumoForm(ModelForm): #Criando o formulario da tabela "Alerta"
    class Meta:
        model = Consumo
        fields = ['h_inicial', 'h_final', 'dias']        
