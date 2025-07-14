from django.urls import path
from galeria.views import index

#Cada aplicação será responsavel por suas urls.

urlpatterns = [
    path('', index),

]