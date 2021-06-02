from django.db import models

# Create your models here.
class Agendamento(models.Model):
    datahora = models.DateTimeField('Data e hora')
    local = models.CharField('Local', max_length=100)
    idade = models.PositiveSmallIntegerField('Idade')
    status = models.CharField('Status', max_length=10)

class Cidadao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data = models.DateField('Data de nascimento')
    email = models.EmailField('Email', max_length=254)
    senha = models.CharField('Senha', max_length=254)

class Grupo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    idade = models.PositiveSmallIntegerField('Idade')
    def __str__(self):
        return f'{self.nome} - {self.idade}+'

class Local(models.Model):
    nome = models.CharField('Nome', max_length=100)
    logradouro = models.CharField('Logradouro', max_length=100)
    bairro = models.CharField('Bairro', max_length=25)
    cidade = models.CharField('Cidade', max_length=25)
    def __str__(self):
        return f'{self.nome} - {self.cidade}'