from django.views.generic import TemplateView
from django.shortcuts import render


def vista_login(request):
    return render(request,"inicio/login.html")