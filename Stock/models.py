from select import select
from typing import Type
from django.db import models

# Create your models here.

class Libelle(models.Model):
    Produit=models.CharField(max_length=30)
    def __str__(self):
        return self.Produit

class Marque(models.Model):
    Type=models.CharField(max_length=30)
    def __str__(self):
        return self.Type


class Produits(models.Model):
    Produit=models.ForeignKey(Libelle, on_delete=models.CASCADE)
    Type=models.ForeignKey(Marque, on_delete=models.CASCADE)
    Quantitee=models.IntegerField(default=0)
    PrixU=models.IntegerField(default=0)
    PrixT=models.IntegerField(default=0)
    def __str__(self):
        return self.Produit.Produit
    

class Vente(models.Model):
    Produit=models.ForeignKey(Produits, on_delete=models.CASCADE)
    Type=models.ForeignKey(Marque, on_delete=models.CASCADE)
    Quantitee=models.IntegerField(default=0)
    PrixU=models.IntegerField(default=0)
    PrixT=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    
   
