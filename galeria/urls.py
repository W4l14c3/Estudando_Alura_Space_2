from django.urls import path
from galeria.views import index, imagem

'''
Cada aplicação será responsavel por suas rotear suas urls.
Aqui somente indicamos as urls da aplicação galeria importando suas funções.
Este arquivo foi incluido no Setup/urls.py(Herança)
'''

urlpatterns = [
    path('', index),
    path('imagem/', imagem)

]