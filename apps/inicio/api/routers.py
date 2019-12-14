from rest_framework import routers
from apps.inicio.api.viewsets import LibroViewSet, ClienteViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'Libros',LibroViewSet,basename='list-libros')
router.register(r'Cliente',ClienteViewSet,basename='list-cliente')
router.register(r'Categoria',CategoriaViewSet,basename='list-categoria')