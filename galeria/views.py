from django.shortcuts import render
#from django.http import HttpResponse lib contem funções de resposta.

#Responsavel pela pagina principal.
#Recebemos uma requisição.
#Após preparar a view para exibir as informaçoes temos que fazer o roteamento.
#Depois de configurar-mos o DIRS em TEMPLATES no setup,
#todas as requisições de pagina irão renderizar automaticamente da pasta templates
#return render(request, 'index.html')-> busca na pasta templates, indicado como diretorio base para templates.



def index(request):
    #Dicionario de dados para as fotos que serão renderizadas por view.
    dados = { 
        1: {"nome": "Nebulosa de Carina", 
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079", 
            "legenda": "nasa.org / NASA / Hubble"}
            }
    return render(request, 'galeria/index.html', {"cards": dados})

#Responsavel por renderizar a pagina imagem.html
def imagem(request):
    return render(request, 'galeria/imagem.html')