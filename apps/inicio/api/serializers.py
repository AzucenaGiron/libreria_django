from apps.inicio.models import Libros,Alquiler,Autor,Categoria,Cliente,Editorial 
from rest_framework import serializers



class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('__all__')

class EditorialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('__all__')

class LibroSerializers(serializers.ModelSerializer):
    categoria = CategoriaSerializers(read_only=True)    
    autor = AutorSerializers(read_only=True)
    editorial = EditorialSerializers(read_only=True)
    
    class Meta:
        model = Libros
        fields = ('__all__')
        #fields = ('id','titulo','categoria','autor','editorial')


class AlquilerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ('__all__')
        

class ClienteSerializers(serializers.ModelSerializer):
    libros = LibroSerializers(read_only=True)
    class Meta:
        model = Cliente
        fields = ('__all__')

