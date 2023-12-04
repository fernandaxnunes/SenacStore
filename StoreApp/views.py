from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
     produtos_em_destaque = Produto.objects.filter(destaque = True)
     context = {
        'produtos' : produtos_em_destaque,
    }

     return render(request, 'index.html', context)

def produto_lista(request):
    
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos,
        'categoria' : 'Todos os produtos'
    }
    return render(request, 'produtos.html', context)

def produto_lista_por_id(request, id):
    #Filtrando
    produtos = Produto.objects.filter(departamento_id = id)
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos,
        'categoria' : departamento.nome
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    context = {
        'produto' : produto
    }

    return render(request, 'produto_detalhes.html',context)
