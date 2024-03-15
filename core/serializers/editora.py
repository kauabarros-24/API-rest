from rest_framework.serializers import ModelSerializer
from core.models import Categoria, Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        mode = Editora
        fields = "__all__"