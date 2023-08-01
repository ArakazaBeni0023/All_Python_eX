from rest_framework import viewsets
from rest_framework.permissions import *

from .models import *
from .serializers import *

class ProduitsViewset(viewsets.ModelViewSet):
    queryset = Produits.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = ProduitsSerializer

    def perform_create(self,serializer):
        serializer.save(utilisateur=self.request.user)
        return serializer

class VentesViewset(viewsets.ModelViewSet):
    queryset = Ventes.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = VentesSerializer

    def perform_create(self,serializer):
        data=serializer.validated_data
        quantite = data ['quantite']
        produit = data['nom']
        prix = produit.prixUnitaire
        serializer.save(totalPrice = quantite * prix)
        return serializer

