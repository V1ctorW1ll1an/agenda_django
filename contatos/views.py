from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request=request, template_name='contatos/index.html', context={
        'contatos': contatos
    })