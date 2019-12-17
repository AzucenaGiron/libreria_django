from django.contrib import admin
from django.urls import path, include
from .api.routers import router
from .views import vista_login,vista_inicio,vista_libros
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',vista_inicio,name='inicio'),
    path('api/',include(router.urls)),
    #path('login/',vista_login,name="vistalogin"),
    path('login/',LoginView.as_view(template_name="inicio/index.html"),name='login'),
    path('cerrar/',LogoutView.as_view(template_name="inicio/login.html"),name="logout"),
    path('libros/',vista_libros,name="libros")
   
]