from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q #para consultas mais complexas

def index(request):

    # contatos = Contato.objects.order_by('nome').filter(
    #     mostrar = True
    # ) # filtros podem ser encadeados 

    contatos = Contato.objects.order_by('nome')
    # contatos = Contato.objects.order_by('-nome') # ordem decrescente

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
    
    if not contato_pelo_id.mostrar:
        raise Http404()

    return render(request=request, template_name='contatos/ver_contato.html', context={
        'contato_pelo_id': contato_pelo_id
    })
    # except Contato.DoesNotExist as e:
    #   raise Http404()


def busca(request):
    termo = request.GET.get('termo')
    contatos = Contato.objects.order_by('nome').filter(
        Q(nome__icontains =termo) | Q(sobrenome__icontains = termo)
    )
    print(contatos.query) # print na query de busca
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request=request, template_name='contatos/busca.html', context={
        'contatos': contatos
    })