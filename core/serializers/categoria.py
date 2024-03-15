from rest_framework.serializers import ModelSerializer
from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        #Define o model que será serializado
        model = Categoria
        #Define que todos os campos serão serializados
        fields = "__all__"