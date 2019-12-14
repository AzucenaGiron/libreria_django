from rest_framework import viewsets
from apps.inicio.api.serializers import LibroSerializers,AlquilerSerializers,AutorSerializers,CategoriaSerializers,ClienteSerializers
from apps.inicio.models import Libros,Alquiler,Autor,Categoria,Cliente

class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializers
    querrset = Libros.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializers
    querrset = Cliente.objects.all()
    
class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializers
    querrset = Categoria.objects.all()