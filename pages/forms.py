from django import forms
from .models import Loja, Servico

class OrdemServicoForm(forms.Form):
    loja = forms.ModelChoiceField(
        queryset=Loja.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    servico = forms.ModelChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

def salvar_ordem_servico(request, form):
    if form.is_valid():
        loja = form.cleaned_data['loja']
        servico = form.cleaned_data['servico']
        # Adicione aqui a lógica para salvar a ordem de serviço