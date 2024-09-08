# form_utils.py
from django import forms

def add_class(fields, css_class):
    for field in fields:
        if isinstance(fields[field].widget, forms.widgets.Input):
            fields[field].widget.attrs.update({'class': css_class})