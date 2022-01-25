from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request=request, template_name='contatos/index.html', context={
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato_pelo_id = Contato.objects.get(id=contato_id)
    return render(request=request, template_name='contatos/ver_contato.html', context={
        'contato_pelo_id': contato_pelo_id
    })