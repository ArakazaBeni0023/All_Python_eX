from django.db import models
# from django.contrib.auth.models import User

class Produits(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=64)
    prixUnitaire = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Produits"

class Ventes(models.Model):
    id = models.BigAutoField(primary_key=True)
    # nom = models.ForeignKey(Produits, on_delete=models.PROTECT)
    quantite = models.IntegerField(unique=True)
    totalPrice = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Ventes"