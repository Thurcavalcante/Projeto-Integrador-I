from .models import Usuario
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'idade', 'cpf']    