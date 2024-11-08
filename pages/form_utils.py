# form_utils.py
from django import forms

def add_class(fields, css_class):# Função para adicionar uma classe CSS a todos os campos de um formulário
    for field in fields:
        if isinstance(fields[field].widget, forms.widgets.Input):
            fields[field].widget.attrs.update({'class': css_class})