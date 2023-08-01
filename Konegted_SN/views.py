from rest_framework import viewsets

from .models import *
from .serializers import *

# class UtilisateurViewset(viewsets.ModelViewSet):
#     queryset = Utilisateur.objects.all()
#     serializer_class = UtilisateurSerializer

class FormateurViewset(viewsets.ModelViewSet):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer

class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class MatierViewset(viewsets.ModelViewSet):
    queryset = Matier.objects.all()
    serializer_class = MatierSerializer    
    
# class ReservationViewset(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer 