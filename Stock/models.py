from select import select
from typing import Type
from django.db import models

# Create your models here.

class Fournisseur(models.Model):
    Nom=models.CharField(max_length=30)
    def __str__(self):
        return self.Nom

class Service(models.Model):
    Nom=models.CharField(max_length=30)
    def __str__(self):
        return self.Nom


class STOCK(models.Model):
    Designation=models.CharField(max_length=30)
    QTEx=models.IntegerField(default=0)
    QTEn=models.IntegerField(default=0)
    QTS=models.IntegerField(default=0)
    QTR=models.IntegerField(default=0)
    def __str__(self):
        return self.Designation
    
class StockEn(models.Model):
    Designation=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    QTEx=models.IntegerField()
    QTEn=models.IntegerField()
    QTR=models.IntegerField()
    Fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
   

class Sorti(models.Model):
    Designation=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    QTEx=models.IntegerField()
    QTS=models.IntegerField()
    QTR=models.IntegerField()
    date=models.DateField(auto_now_add=True)


