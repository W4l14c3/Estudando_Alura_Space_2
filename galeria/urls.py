from django.urls import path
from galeria.views import index, imagem, buscar

'''
Cada aplicação será responsavel por suas rotear suas urls.
Aqui somente indicamos as urls da aplicação galeria importando suas funções.
Este arquivo foi incluido no Setup/urls.py(Herança)

Agora o Django encontra o caminho para executar as funções da views, através do name, 
pois os links estão com codigo embedado python.

'''

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name='buscar'),

]