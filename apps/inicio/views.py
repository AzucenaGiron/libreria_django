from django.views.generic import TemplateView
from django.shortcuts import render


def vista_login(request):
    return render(request,"inicio/login.html")
def vista_inicio(request):
    return render(request,"inicio/index.html")
def vista_libros(request):
    return render(request,"libros/libros.html")    