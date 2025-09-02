from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia

#from django.http import HttpResponse lib contem funções de resposta.

#Responsavel pela pagina principal.
#Recebemos uma requisição.
#Após preparar a view para exibir as informaçoes temos que fazer o roteamento.
#Depois de configurar-mos o DIRS em TEMPLATES no setup,
#todas as requisições de pagina irão renderizar automaticamente da pasta templates
#return render(request, 'index.html')-> busca na pasta templates, indicado como diretorio base para templates.



def index(request):
    #Comando que vai buscar todos os objetos no modelo Fotografia.
    #E manda para a variavel fotografias.
    #Ordena por data e filtra por verdadeiro
    fotografias = Fotografia.objects.order_by("data_edicao").filter(publicada = True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

#Responsavel por renderizar a pagina imagem.html
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)#Pega o objeto ou retorna um erro 404
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia}) 

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_edicao").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards": fotografias})