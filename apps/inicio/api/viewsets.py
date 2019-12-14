from rest_framework import viewsets
from apps.inicio.api.serializers import LibroSerializers,AlquilerSerializers,AutorSerializers,CategoriaSerializers,ClienteSerializers,EditorialSerializers
from apps.inicio.models import Libros,Alquiler,Autor,Categoria,Cliente,Editorial

class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializers
    queryset = Libros.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializers
    queryset = Cliente.objects.all()
    
class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.all()

class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializers
    queryset = Autor.objects.all()

class EditorialViewSet(viewsets.ModelViewSet):
    serializer_class = EditorialSerializers
    queryset = Editorial.objects.all()

class AlquilerViewSet(viewsets.ModelViewSet):
    serializer_class = AlquilerSerializers
    queryset = Alquiler.objects.all()