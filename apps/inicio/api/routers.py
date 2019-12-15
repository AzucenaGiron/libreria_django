from rest_framework import routers
from apps.inicio.api.viewsets import LibroViewSet,ClienteViewSet,CategoriaViewSet,AutorViewSet,EditorialViewSet,AlquilerViewSet

router = routers.DefaultRouter()
router.register(r'Libros',LibroViewSet,basename='list-libros')
router.register(r'Cliente',ClienteViewSet,basename='list-cliente')
router.register(r'Categoria',CategoriaViewSet,basename='list-categoria')
router.register(r'Autor',AutorViewSet,basename='list-autor')
router.register(r'Editorial',EditorialViewSet,basename='list-editorial')
router.register(r'Alquiler',AlquilerViewSet,basename='list-alquiler')