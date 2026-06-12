from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def minha_view(request):
     return HttpResponse("Esta é a minha view!")


def produtos_view(request):
    title = "Lista de Produtos"
    return render(request, 'produtos.html', {'title': title})


def produtos_view2(request):
    itens = ["Notebook", "Mouse", "Teclado", "Monitor"]
    contexto = {
        "title": "Loja Tech",
        "itens_list": itens,
        "total": len(itens)
    }
    return render(request, 'produtos.html', contexto)

def sobre_nos(request):

    contexto = {
        "nome": "Loja Tech",
        "ano": "2007",
        "serviços": ["manutenção", "vendas","formatação"]
    }
    return render(request, 'sobre.html', contexto)

