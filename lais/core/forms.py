from django import forms

class CidadaoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    data = forms.DateField(label='Data de nascimento', required=True)
    email = forms.EmailField(label='Email', required=True)
    senha = forms.CharField(label='Senha', required=True)
    confirmarsenha = forms.CharField(label='Confirmar senha', required=True)