from django.contrib import admin

from apps.inicio.models import Libros, Categoria, Cliente, Alquiler, Editorial, Autor

# Register your models here.

admin.site.register(Libros)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Alquiler)
admin.site.register(Editorial)
admin.site.register(Autor)