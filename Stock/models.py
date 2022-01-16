from typing import Type
from django.db import models

# Create your models here.

class Produits(models.Model):
    Produit=models.CharField(max_length=30)
    Type=models.CharField(max_length=30)
    Quantitee=models.IntegerField(default=0)
    PrixU=models.IntegerField(default=0)
    PrixT=models.IntegerField(default=0)
    def __str__(self):
        return self.Produit

class Vente(models.Model):
    Produit=models.ForeignKey(Produits, on_delete=models.CASCADE)
    Type=models.CharField(max_length=30)
    Quantitee=models.IntegerField(default=0)
    PrixU=models.IntegerField(default=0)
    PrixT=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Vente.name
   