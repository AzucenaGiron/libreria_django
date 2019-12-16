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

class ClienteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ('__all__')

class AlquilerSerializers(serializers.ModelSerializer):
    libro = LibroSerializers(read_only=True)
    libroId = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Libros.objects.all(),source='libro')
    cliente = ClienteSerializers(read_only=True)
    clienteId = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Cliente.objects.all(),source='cliente')
    class Meta:
        model = Alquiler
        fields = ('__all__')
        



