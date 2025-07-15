from django.urls import path
from galeria.views import index, imagem

#Cada aplicação será responsavel por suas urls.

urlpatterns = [
    path('', index),
    path('imagem/', imagem)

]