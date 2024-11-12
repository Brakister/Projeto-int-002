from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import OrdemServicoForm, UserRegistrationForm
from .models import EmissaoOrdemServico
from openpyxl import Workbook
from django.http import HttpResponse

def home(request):# Função para exibir a página inicial e utilizar o formulário de login
    if request.user.is_authenticated:
        return redirect('principal')
    return render(request, 'pages/home.html')
def login(request):
    return render(request, 'pages/registration/login.html')
@login_required
def criar_ordem_servico(request):# Função para criar uma ordem de serviço
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['loja']
            servico = form.cleaned_data['servico']
            numero_os = form.cleaned_data['numero_os'] 
            user = request.user
            EmissaoOrdemServico.objects.create(empresa=empresa, servico=servico, numero_os=numero_os, usuario=user)
            return redirect('ordem_servico_confirmacao') # Redirecione para a página de confirmação
    else:
        form = OrdemServicoForm()
    return render(request, 'pages/ordem_servico/ordem_servico_registro.html', {'form': form})


@login_required
def principal(request):# Função para exibir a página principal
    return render(request, 'pages/principal.html')

def historico_ordem_servico(request, mes=None):
    if mes:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
    return render(request, 'pages/ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico})

def baixar_excel(request, mes):# Função para baixar um arquivo excel com as ordens de serviço
    
    wb = Workbook()
    ws = wb.active 
    ws.append(['Numero Os','Empresa', 'Serviço', 'Data', 'Usuario'])

    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    for ordem in ordens_servico:
        
        data_sem_fuso_horario = ordem.data.replace(tzinfo=None)
        ws.append([ordem.numero_os, ordem.empresa, ordem.servico, data_sem_fuso_horario, ordem.usuario.username])

    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    response['Content-Disposition'] = f'attachment; filename=ordens_servico_{mes}.xlsx'
    
    wb.save(response)

    return response

def historico_ordem_servico(request, mes=None):# Função para exibir o histórico de ordens de serviço
    if mes and 1 <= 12:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
        mes = 1 
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)

    return render(request, 'pages/ordem_servico/historico_ordem_servico.html', {
        'ordens_servico': ordens_servico,
        'mes': mes
    })

def emitir_planilha(request, mes, ano):# Função para emitir uma planilha de ordens de serviço
    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes, data__year=ano)



   
    planilha = "Planilha de Ordens de Serviço para o mês {} do ano {}\n".format(mes, ano)
    for ordem in ordens_servico:
        planilha += "Empresa: {}, Serviço: {}, Data: {}\n".format(ordem.empresa, ordem.servico, ordem.data)

    
    return HttpResponse(planilha, content_type='text/plain')
    return response

def ordem_servico_confirmacao(request):# Função para exibir a página de confirmação
    return render(request, 'pages/ordem_servico/ordem_servico_confirmacao.html')

def profile(request):
    return render(request, 'pages/principal.html')
def proposta(request):
    return render(request, 'pages/grup1/teste01.html')

def register(request):# Função para registrar um novo usuário
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserRegistrationForm()
    return render(request, 'pages/registration/register.html', {'form': form})