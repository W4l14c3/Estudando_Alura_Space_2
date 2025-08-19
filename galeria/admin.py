from django.contrib import admin
from galeria.models import Fotografia

#Permite a personalização da pagina admin.
class ListandoFotografias(admin.ModelAdmin):

    list_display = ("id", "nome", "legenda", "publicada")#Cria uma lista de exibição.
    list_display_links = ("id", "nome")#Torna alguns campos lincados.
    search_fields = ("nome",)#Adiciona um campo de busca.
    list_filter = ("categoria",)#Adiciona um filtro no admin.
    list_editable = ("publicada",)
    list_per_page = 5


#Toda nova classe criada deve ser adicionada no register para aplicar as mudanças.
admin.site.register(Fotografia, ListandoFotografias)
