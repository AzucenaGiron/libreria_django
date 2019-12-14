from django.contrib import admin
from django.urls import path, include
from .api.routers import router
#from .views import inicio_vista

urlpatterns = [
    #path('',inicio_vista,name='inicio'),
    path('api/',include(router.urls)),
]
