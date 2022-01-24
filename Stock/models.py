from select import select
from typing import Type
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Admin = models.BooleanField(default=False)
    Utilisateur = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Utilisateurs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
'''

class Utlisateur(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.EmailField(max_length=220)
    login=models.CharField(max_length=220)
    Password=models.IntegerField()
    Type=models.CharField(max_length=220)
    Stock=models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
'''
class Fournisseur(models.Model):
    Nom=models.CharField(max_length=30)
    Abrevation=models.CharField(max_length=30)
    NomDirecteur=models.CharField(max_length=30)
    Nif=models.IntegerField()
    Tel=models.IntegerField()
    Email=models.CharField(max_length=30)
    Domaine=models.CharField(max_length=30)
    RC=models.IntegerField()

    def __str__(self):
        return self.Nom

class Service(models.Model):
    Nom=models.CharField(max_length=30)
    def __str__(self):
        return self.Nom



class STOCK(models.Model):
    Designation=models.CharField(max_length=30)
    QTEx=models.IntegerField(default=0)
    def __str__(self):
        return self.Designation
    
class StockEn(models.Model):
    Designation=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    QTEx=models.IntegerField()
    QTEn=models.IntegerField()
    Fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    #Utlisateur=models.ForeignKey(Utlisateur, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
   

class Sorti(models.Model):
    Designation=models.ForeignKey(STOCK, on_delete=models.CASCADE)
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    QTS=models.IntegerField()
    QTR=models.IntegerField()
   # Utlisateur=models.ForeignKey(Utlisateur, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)




class STOCKfm(models.Model):
    Designation=models.CharField(max_length=30)
    QTEx=models.IntegerField(default=0)
    def __str__(self):
        return self.Designation

class StockEnfm(models.Model):
    Designation=models.ForeignKey(STOCKfm, on_delete=models.CASCADE)
    QTEx=models.IntegerField()
    QTEn=models.IntegerField()
    Fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    Stock=models.ForeignKey(STOCK,on_delete=models.CASCADE)
    #Utlisateur=models.ForeignKey(Utlisateur, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
   

class Sortifm(models.Model):
    Designation=models.ForeignKey(STOCKfm, on_delete=models.CASCADE)
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    QTS=models.IntegerField()
    QTR=models.IntegerField()
    #Utlisateur=models.ForeignKey(Utlisateur, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)


