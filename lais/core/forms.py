from django import forms

class CidadaoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    data = forms.DateField(label='Data de nascimento', required=True)
    email = forms.EmailField(label='Email', max_length=254, required=True)
    senha = forms.CharField(label='Senha', max_length=254, required=True)
    confirmarsenha = forms.CharField(label='Confirmar senha', max_length=254, required=True)