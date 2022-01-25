from re import search
from typing import Container
from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    search_fields = ('nome',)
    # ... entre outros filtros

admin.site.register(Categoria)
admin.site.register(Contato , ContatoAdmin)