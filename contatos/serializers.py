from rest_framework.serializers import ModelSerializer
from .models import Amigo


class AmigoSerializer(ModelSerializer):
    class Meta:
        model = Amigo
        fields = "__all__"
