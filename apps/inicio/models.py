from django.db import models

# Create your models here.
class Categoria(models.Model):

    categoria = models.CharField(max_length=100, blank = True, null =True)

class Editorial(models.Model):

    editorial = models.CharField(max_length=100, blank = True, null =True)
    fecha = models.DateField()
    año = models.DateField()

class Autor(models.Model):  

    nombre = models.CharField(max_length=100, blank = True, null =True)
    apellidoM = models.CharField(max_length=100, blank = True, null =True)
    apellidoP = models.CharField(max_length=100, blank = True, null =True)

class Libros(models.Model):

    titulo = models.CharField(max_length=100, blank = True, null =True)   
    categoria = models.ForeignKey(Categoria,max_length=100, blank = True, null =True,on_delete= models.CASCADE)
    autor = models.ForeignKey(Autor,max_length=100, blank = True, null =True, on_delete= models.CASCADE)
    editorial = models.ForeignKey(Editorial,max_length=100, blank = True, null =True,on_delete=models.CASCADE)

class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100, blank = True, null =True)
    apellidoM = models.CharField(max_length=100, blank = True, null =True)
    apellidoP = models.CharField(max_length=100, blank = True, null =True)
    direccion = models.CharField(max_length=100, blank = True, null =True)
    telefono = models.CharField(max_length=100, blank = True, null =True)
    libro = models.ManyToManyField(Libros,max_length=100, blank = True, null =True)

class Alquiler(models.Model):

    #fechaSalida = models.DateField()
    #fechaEntrada = models.DateField()
    cliente = models.ForeignKey(Cliente, blank = True, null =True,on_delete=models.SET_NULL, related_name='cliente')
    libro = models.ForeignKey(Libros,blank = True, null =True,on_delete=models.SET_NULL,related_name='libro')







