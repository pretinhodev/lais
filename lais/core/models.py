from django.db import models

# Create your models here.
class Agendamento(models.Model):
    datahora = models.DateTimeField('Data e hora', auto_now=True)
    local = models.CharField('Local', max_length=100)
    idade = models.PositiveSmallIntegerField('Idade')
    status = models.CharField('Status', max_length=10)