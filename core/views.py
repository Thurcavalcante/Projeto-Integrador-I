from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
from .forms import UsuarioForm, AlertaForm, ConsumoForm #importando a class criado em forms.py 
from django.contrib.auth.models import User
from .models import Usuario, Alerta, Consumo
# Create your views here.

def home(request):
    return render(request, 'index.html')

#def cadastro(request):
    #return render(request, 'cadastro.html')

# def login(request):
#     return render(request, 'login.html')   

@login_required #Para que somente usuários autenticados acessem o template perfil, em views adicionar a anotação @login_required
def painel(request):
    return render(request, 'painel.html') 

def painel2(request):
    return render(request, 'painel2.html')      

def autenticacao(request):
    '''
    se o usuário digitou algo no formulário e clicou em enviar, o if 
    será verdadeiro, caso contrário, será uma requisição GET e entrara no else.
    -
    '''
    if request.POST:
       usuario = request.POST['usuario']
       senha = request.POST['senha']
       user = authenticate(request, username=usuario, password=senha)
       if user is not None:
        login(request, user)
        return redirect('painel')
       else:
        return redirect('login') 
    else:
        return render(request, 'registration\login.html') 

def desconectar(request):
    logout(request)
    return render(request, 'index.html')  


def cadastro_manual(request):
    user = Usuario.objects.create_user(
        username='admin02',
        email='admin02@email.com',
        cpf='22222222222',
        nome='Administrador02',
        password='admin222',
        idade=30,
        is_superuser=False)
        
     #permission = Permission.objects.get(codename='permissao_adm_1') #adicionando ssds a permissao: permissao_adm_1, a este usuario == Podemos criar novos usuarios que não sejam administradores e não damos essas permissões a ele
     #user.user_permissions.add(permission)
    permission1 = Permission.objects.get(codename='permissao_adm_1')
    permission2 = Permission.objects.get(codename='permissao_adm_2')
    user.user_permissions.add(permission1, permission2)


    user.save()
    return redirect('home')   

@login_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
@permission_required('core.permissao_adm_1')
def pagina_usuarios(request): 
    return render(request, 'usuarios.html')     


#REGISTRO
def registro(request):
    form = UsuarioForm(request.POST or None) #Inplemantando o registro utilizando a class criada emm 'forms.py'
    if form.is_valid(): #Ao realizar o registro, automaticamente o usuário será redirecionado para a página de login:
        form.save()
        return redirect('login')
    contexto = {
        'form': form
        }
    return render(request, 'registro.html', contexto)


#MEUS DADOS - a função dados que exibirá os dados do usuário em um formulário (primeiro acesso), e também poderá atualizar os dados (caso ele faça alguma alteração e salve):

@login_required
def dados(request, cpf):
    user = Usuario.objects.get(pk=cpf)
    form = UsuarioForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()   
        return redirect('painel')
    contexto = {
        'form': form
    }    
    return render(request, 'registro.html', contexto)



#Alerta
@login_required 
def listar_alerta(request):       
    alerta = Alerta.objects.all()
    contexto = {
        'todos_alerta': alerta
    }
    return render (request, 'alerta.html', contexto)


@login_required 
def cadastrar_alerta(request):     
    form = AlertaForm(request.POST or None)

    if form.is_valid(): #Se os dados forem validos, salve o formulario..
        form.save()
        return redirect('listar_alerta') # e redirecione o usuario para pagina de listagem

    contexto = {
        'form_alerta': form
    }
    return render(request, 'alerta_cadastrar.html', contexto)


@login_required 
def editar_alerta(request, id): #EDITAR dados do ALERTA
    alerta = Alerta.objects.get(pk=id)

    form = AlertaForm(request.POST or None, instance=alerta)

    if form.is_valid():
        form.save()
        return redirect('listar_alerta')

    contexto = {
        'form_alerta': form
    }    

    return render (request, 'alerta_cadastrar.html', contexto)

@login_required 
def remover_alerta(request, id): 
    alerta = Alerta.objects.get(pk=id)
    alerta.delete()
    return redirect('listar_alerta')


#Consumo
@login_required 
def listar_consumo(request):       
    consumo = Consumo.objects.all()
    contexto = {
        'todos_consumo': consumo
    }
    return render (request, 'consumo.html', contexto)


@login_required 
def cadastrar_consumo(request):     
    form = ConsumoForm(request.POST or None)

    if form.is_valid(): #Se os dados forem validos, salve o formulario..
        form.save()
        return redirect('listar_consumo') # e redirecione o usuario para pagina de listagem

    contexto = {
        'form_consumo': form
    }
    return render(request, 'consumo_cadastrar.html', contexto)

@login_required 
def editar_consumo(request, id): #EDITAR dados do CONSUMO
    consumo = Consumo.objects.get(pk=id)

    form = ConsumoForm(request.POST or None, instance=consumo)

    if form.is_valid():
        form.save()
        return redirect('listar_consumo')

    contexto = {
        'form_consumo': form
    }    

    return render (request, 'consumo_cadastrar.html', contexto)

@login_required 
def remover_consumo(request, id): 
    consumo = Consumo.objects.get(pk=id)
    consumo.delete()
    return redirect('listar_consumo')  