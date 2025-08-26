from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

'''from galeria.views import index
Isso é responsabilidade agora da aplicação galeria!!
Cada aplicação cuidara do roteamento individualmente.

Aqui é onde fazemos o roteamento das aplicações e seus arquivos url.
Quando ocorre uma requisição ela é recebida pela urls.py,
que procura o a aplicação correspondente que vai ser responsavel por ministrar a requisição no urlpatterns.
que ira devolver o conteudo, mas para isso acontecer temos que indicar a rota
como esta por exemplo: path('', index) indica que quando etiver-mos na pagina raiz
execute a função index

Agora cada aplicação será responsavel por suas urls, nesse caso, ao invés de,
colocarmos cada função referente a requisição do usuario aqui, 
e incluimos apenas o arquivo de roteamento de cada aplicação,
pois la terão as funções com as requisições e suas respostas.

Esses comentarios são só pela didatica, o certo seriam os codigos serem 
auto explicativos, regra de boa pratica e clean code!'''

urlpatterns = [
    path('admin/', admin.site.urls),
    #Abaixo, navegamos da pasta galeria até o arquivo urls.py e herdamos tudo.
    path('', include('galeria.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
