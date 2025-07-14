from django.contrib import admin
from django.urls import path
from galeria.views import index

#Aqui é onde fazemos o roteamento das aplicações.
#Quando ocorre uma requisição ela é recebida pela urls.py que procura o padrão correspondente.
#Que ira devolver o conteudo, mas para isso acontecer temos que indicar a rota.
#Como esta: path('', index) indica que quando etiver-mos na pagina raiz.
#Execute a função index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
