from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    #define o conjunto de objetos que será retornado pela view.
    queryset = Categoria.objects.all()
    #define o serializer que será utilizado para serializar os objetos
    serializer_class = CategoriaSerializer