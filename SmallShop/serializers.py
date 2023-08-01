from rest_framework import serializers
from .models import *

class ProduitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produits
        fields = "__all__"
   
class VentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventes
        fields = "__all__"
        read_only_fields = "totalPrice",
    