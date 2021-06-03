from typing_extensions import Required
from django import forms
from django.forms import widgets

class CidadaoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    data = forms.DateField(label='Data de nascimento', required=True)
    email = forms.EmailField(label='Email', required=True)
    senha = forms.CharField(label='Senha', required=True, widgets=forms.PasswordInput())
    confirmarsenha = forms.CharField(label='Confirmar senha', required=True, widgets=forms.PasswordInput())