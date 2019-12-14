from apps.inicio.models import Libros,Alquiler,Autor,Categoria,Cliente 
from rest_framework import serializers

class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ('__all__')

class AlquilerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ('__all__')

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')