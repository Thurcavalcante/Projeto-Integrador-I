from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
from .forms import UsuarioForm, AlertaForm, ConsumoForm, ResidenciaForm, CategoriaForm, Periodo_Consumo_AlertaForm #importando a class criado em forms.py 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usuario, Alerta, Consumo, Residencia, Categoria, Periodo_Consumo_Alerta
# Create your views here.

def home(request):
    return render(request, 'index.html')  

# botao acessar
def painel_sessao(request, id):
    request.session['residencia_id'] = id
    return redirect('painel')

@login_required 
def painel(request):
    if request.session.get('residencia_id', None):
        id = request.session['residencia_id']
        residencia = Residencia.objects.get(id=id)
        print("Id = " + str(id))
        print("residencia = " + residencia.apelido)
        contexto = {
            'residencia_sessao': residencia
        }
        return render(request, 'painel.html', contexto)
    else:
        return redirect('listar_residencia') 


   

def painel2(request):
    return render(request, 'painel2.html')      

def perfil(request):
    return render(request, 'perfil.html')

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
        messages.success(request, 'Bem-vindo(a)') #corrigir
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
        username='admin03',
        email='admin03@email.com',
        cpf='333333333',
        nome='Administrador03',
        password='admin333',
        idade=26,
        categoria = Categoria.objects.get(pk=1),
        is_superuser=False)
        

    permission1 = Permission.objects.get(codename='permissao_adm_1')
    permission2 = Permission.objects.get(codename='permissao_adm_2')
    permission3 = Permission.objects.get(codename='permissao_adm_3')
    user.user_permissions.add(permission1, permission2, permission3)


    user.save()
    return redirect('home')   

    #Se for modificar um usuario
    # user = Usuario.objects.get(pk='22222222222')
    # permission3 = Permission.objects.get(codename='permissao_adm_3')
    # user.user_permissions.add(permission3)
    # user.save()
    # return redirect('home')  

@login_required 
@permission_required('core.permissao_adm_1') 
def pagina_usuarios(request, categoria_url): 
    #Listar usuarios do BD
    if categoria_url == 'todos':
        todos_usuarios = Usuario.objects.all()
    else:
        todos_usuarios = Usuario.objects.filter(categoria=categoria_url)
    
    todas_categorias = Categoria.objects.all()

    contexto = {
        'todos_usuarios' : todos_usuarios,
        'todas_categorias': todas_categorias,
        'categoria_selecionada': categoria_url
    }
    return render(request, 'usuarios.html', contexto)     


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
    alerta = Alerta.objects.filter(residencia__id = request.session['residencia_id'])
    contexto = {
        'todos_alerta': alerta
    }
    return render (request, 'alerta.html', contexto)


@login_required 
def cadastrar_alerta(request):     
    form = AlertaForm(request.POST or None)
    if form.is_valid():
        alerta = form.save(commit=False)
        alerta.residencia = Residencia.objects.get(pk=request.session['residencia_id'])
        alerta.save()
        return redirect('listar_alerta') 

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
    consumo = Consumo.objects.filter(residencia__id = request.session['residencia_id'])
    contexto = {
        'todos_consumo': consumo
    }
    return render (request, 'consumo.html', contexto)


@login_required 
def cadastrar_consumo(request): 
    form = ConsumoForm(request.POST or None)
    if form.is_valid(): 
        consumo = form.save(commit=False)
        consumo.residencia = Residencia.objects.get(pk=request.session['residencia_id'])
        consumo.save()
        return redirect('listar_consumo') 

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



#Residencia 
@login_required 
def listar_residencia(request):       
    residencia = Residencia.objects.filter(usuario=request.user)
    contexto = {
        'todas_residencia': residencia
    }
    return render (request, 'residencia.html', contexto)


@login_required 
def cadastrar_residencia(request):     
    form = ResidenciaForm(request.POST or None)
    if form.is_valid(): 
        residencia = form.save(commit=False)
        residencia.usuario = request.user
        residencia.save()
        return redirect('listar_residencia') 

    contexto = {
        'form_residencia': form
    }
    return render(request, 'residencia_cadastrar.html', contexto)

@login_required 
def editar_residencia(request, id): #EDITAR dados da residencia
    residencia = Residencia.objects.get(pk=id)

    form = ResidenciaForm(request.POST or None, instance=residencia)

    if form.is_valid():
        form.save()
        return redirect('listar_residencia')

    contexto = {
        'form_residencia': form
    }    

    return render (request, 'residencia_cadastrar.html', contexto)

@login_required 
def remover_residencia(request, id): 
    residencia = Residencia.objects.get(pk=id) 
    residencia.delete()
    return redirect('listar_residencia')      




#Categoria
@login_required 
@permission_required('core.permissao_adm_3')
def listar_categoria(request):       
    categoria = Categoria.objects.all()
    contexto = {
        'todas_categoria': categoria
    }
    return render (request, 'categoria.html', contexto)


@login_required 
@permission_required('core.permissao_adm_3')
def cadastrar_categoria(request):     
    form = CategoriaForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('listar_categoria') 

    contexto = {
        'form_categoria': form
    }
    return render(request, 'categoria_cadastrar.html', contexto)


@login_required 
@permission_required('core.permissao_adm_3')
def editar_categoria(request, id): #EDITAR nome da categoria
    categoria = Categoria.objects.get(pk=id)

    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listar_categoria')

    contexto = {
        'form_categoria': form
    }    

    return render (request, 'categoria_cadastrar.html', contexto)


@login_required 
@permission_required('core.permissao_adm_3')
def remover_categoria(request, id): 
    categoria = Categoria.objects.get(pk=id) 
    categoria.delete()
    return redirect('listar_categoria') 





















#Periodo do alerta
@login_required 
@permission_required('core.permissao_adm_3')
def listar_periodoalerta(request):       
    periodoalerta = Periodo_Consumo_Alerta.objects.all()
    contexto = {
        'todos_periodoalerta': periodoalerta
    }
    return render (request, 'periodoalerta.html', contexto)


@login_required
@permission_required('core.permissao_adm_3')
def cadastrar_periodoalerta(request):     
    form = Periodo_Consumo_AlertaForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('listar_periodoalerta')

    contexto = {
        'form_periodoalerta': form
    }
    return render(request, 'periodoalerta_cadastrar.html', contexto)


@login_required 
@permission_required('core.permissao_adm_3')
def editar_periodoalerta(request, id): #EDITAR nome do periodoalerta
    periodoalerta = Periodo_Consumo_Alerta.objects.get(pk=id)

    form = Periodo_Consumo_AlertaForm(request.POST or None, instance=periodoalerta)

    if form.is_valid():
        form.save()
        return redirect('listar_periodoalerta')

    contexto = {
        'form_periodoalerta': form
    }    

    return render (request, 'periodoalerta_cadastrar.html', contexto)


@login_required 
@permission_required('core.permissao_adm_3')
def remover_periodoalerta(request, id): 
    periodoalerta = Periodo_Consumo_Alerta.objects.get(pk=id) 
    periodoalerta.delete()
    return redirect('listar_periodoalerta')

