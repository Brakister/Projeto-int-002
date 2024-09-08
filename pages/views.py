from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import OrdemServicoForm
from .models import EmissaoOrdemServico
from openpyxl import Workbook
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('principal')
    return render(request, 'pages/home.html')
def login(request):
    return render(request, 'pages/registration/login.html')
@login_required
def criar_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['loja']
            servico = form.cleaned_data['servico']         
            EmissaoOrdemServico.objects.create(empresa=empresa, servico=servico)
            return redirect('ordem_servico_confirmacao') # Redirecione para a página de confirmação
    else:
        form = OrdemServicoForm()
    return render(request, 'pages/ordem_servico/ordem_servico_registro.html', {'form': form})


@login_required
def principal(request):
    return render(request, 'pages/principal.html')

def historico_ordem_servico(request, mes=None):
    if mes:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
    return render(request, 'ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico})

def baixar_excel(request, mes):
    
    wb = Workbook()
    ws = wb.active 
    ws.append(['Empresa', 'Serviço', 'Produto', 'Data'])

    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    for ordem in ordens_servico:
        
        data_sem_fuso_horario = ordem.data.replace(tzinfo=None)
        ws.append([ordem.empresa, ordem.servico, ordem.produto, data_sem_fuso_horario])

    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    response['Content-Disposition'] = f'attachment; filename=ordens_servico_{mes}.xlsx'
    
    wb.save(response)

    return response

def historico_ordem_servico(request, mes=None):
    if mes and 1 <= 12:
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    else:
        ordens_servico = EmissaoOrdemServico.objects.all()
        mes = 1 
        ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes)
    return render(request, 'pages/ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico, 'mes': mes})
   
def emitir_planilha(request, mes, ano):
    
    ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes, data__year=ano)



   
    planilha = "Planilha de Ordens de Serviço para o mês {} do ano {}\n".format(mes, ano)
    for ordem in ordens_servico:
        planilha += "Empresa: {}, Serviço: {}, Data: {}\n".format(ordem.empresa, ordem.servico, ordem.data)

    
    return HttpResponse(planilha, content_type='text/plain')
    return response

def ordem_servico_confirmacao(request):
    return render(request, 'pages/ordem_servico/ordem_servico_confirmacao.html')

def profile(request):
    return render(request, 'pages/principal.html')
def proposta(request):
    return render(request, 'pages/grup1/teste01.html')

