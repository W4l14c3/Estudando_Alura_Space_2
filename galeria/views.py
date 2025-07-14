from django.shortcuts import render
from django.http import HttpResponse #lib contem funções de resposta.

#Responsavel pela pagina principal.
#Recebemos uma requisição.
#Após preparar a view para exibir as informaçoes temos que fazer o roteamento.
def index(request):
    return HttpResponse('<h1>Aluar Space<h1>')
