from django.contrib import admin
from django.urls import path
from galeria.views import index

#Aqui é onde fazemos o roteamento das aplicações.

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', index),
]
