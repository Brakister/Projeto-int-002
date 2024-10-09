from django import forms
from .models import Loja, Servico, OrdemServico  # Certifique-se de importar o modelo OrdemServico
from django.contrib.auth.models import User

class OrdemServicoForm(forms.Form):
    loja = forms.ModelChoiceField(
        queryset=Loja.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    servico = forms.ModelChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    numero_os = forms.CharField(  # Campo para o número da OS
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da OS'})
    )

def salvar_ordem_servico(request, form):
    if form.is_valid():
        loja = form.cleaned_data['loja']
        servico = form.cleaned_data['servico']
        numero_os = form.cleaned_data['numero_os']  # Captura o número da OS
        
        # Cria a nova ordem de serviço e salva no banco de dados
        ordem_servico = OrdemServico(
            loja=loja,
            servico=servico,
            numero_os=numero_os
        )
        ordem_servico.save()  # Salva a ordem de serviço

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
