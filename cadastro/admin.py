from django.contrib import admin

from cadastro.models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'sobrenome',
        'sexo',
        'altura',
        'peso',
        'nascimento',
        'bairro',
        'cidade',
        'estado',
        'numero',
    ]
    list_display = ['id', 'nome', 'sobrenome', 'sexo', 'nascimento', 'cidade']


admin.site.register(Cadastro, CadastroAdmin)
