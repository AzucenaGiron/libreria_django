from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharFiel(max_length=100, blank = True, null =True)
    apellidoM = models.CharField(max_length=100, blank = True, null =True)
    apellidoP = models.CharField(max_length=100, blank = True, null =True)
    direccion = models.CharField(max_length=100, blank = True, null =True)
    telefono = models.CharField(max_length=100, blank = True, null =True)

class Alquiler(models.Model):

    fechaSalida = models.CharField(max_length=100, blank = True, null =True)
    fechaEntrada = models.CharField(max_length=100, blank = True, null =True)
    cliente = models.ForeignKey(Cliente, blank = True, null =True,on_delete=models.SET_NULL)
    libro = models.ForeignKey(Libro,blank = True, null =True,on_delete=models.SET_NULL)


class Categoria(models.Model):

    categoria = models.CharField(max_length=100, blank = True, null =True)

class Editorial(models.Model):

    editorial = models.CharField(max_length=100, blank = True, null =True)
    fecha = models.DataField()
    año = models.DataField()

class Autor(models.Model):  

    nombre = models.CharField(max_length=100, blank = True, null =True)
    apellidoM = models.CharField(max_length=100, blank = True, null =True)
    apellidoP = models.CharField(max_length=100, blank = True, null =True)

class Libros(models.Model):

    titulo = models.CharField(max_length=100, blank = True, null =True)   
    categoria = models.ForeignKey(max_length=100, blank = True, null =True)
    autor = models.ForeignKey(max_length=100, blank = True, null =True)
    editorial = models.ForeignKey(max_length=100, blank = True, null =True)







