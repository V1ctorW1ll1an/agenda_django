from re import search
from typing import Container
from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome','telefone', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    search_fields = ('nome',)
    # ... entre outros filtros
    list_editable= ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato , ContatoAdmin)