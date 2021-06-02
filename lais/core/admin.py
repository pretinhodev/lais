from django.contrib import admin
from .models import Grupo, Local

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')

class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logradouro', 'bairro', 'cidade')

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Local, LocalAdmin)