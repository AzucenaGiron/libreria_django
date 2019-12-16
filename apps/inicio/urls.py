from django.contrib import admin
from django.urls import path, include
from .api.routers import router
from .views import vista_login
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    #path('',inicio_vista,name='inicio'),
    path('api/',include(router.urls)),
    #path('login/',vista_login,name="vistalogin"),
    path('login/',LoginView.as_view(template_name="libros/libros.html"),name='login'),
    path('cerrar/',LogoutView.as_view(template_name="inicio/login.html"),name="logout"),
]
