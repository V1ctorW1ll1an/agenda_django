from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator

def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request=request, template_name='contatos/index.html', context={
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # try:
    # contato_pelo_id = Contato.objects.get(id=contato_id)
    contato_pelo_id = get_object_or_404(Contato, id=contato_id)
    return render(request=request, template_name='contatos/ver_contato.html', context={
        'contato_pelo_id': contato_pelo_id
    })
    # except Contato.DoesNotExist as e:
    #   raise Http404()