from django.contrib import admin
from django.urls import path, include

#from galeria.views import index
#Isso é responsabilidade agora da aplicação galeria!!

#Aqui é onde fazemos o roteamento das aplicações.
#Quando ocorre uma requisição ela é recebida pela urls.py que procura o padrão correspondente
#que ira devolver o conteudo, mas para isso acontecer temos que indicar a rota
#como esta: path('', index) indica que quando etiver-mos na pagina raiz
#execute a função index

#Agora cada aplicação será responsavel por suas urls, nesse caso, ao invés de,
#colocarmos cada função referente a requisição do usuario aqui, colocamos somente a url da aplicação,
#pois la terá essas função com as requisições e suas respostas.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
