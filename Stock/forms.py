from django import forms
from django.forms.widgets import Widget
from .models import Marque, Produits, Vente,Libelle


class LEnregistrer(forms.ModelForm):
     class Meta:
        model = Libelle
        fields = [
            'Produit'
        ]

        widgets = {
            'Produit': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Produit'
            }),     
            
        }

class MEnregistrer(forms.ModelForm):
     class Meta:
        model = Marque
        fields = [
            'Type'
        ]

        widgets = {
            'Type': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Type'
            }),     
            
        }



class PEnregistrer(forms.ModelForm):
    class Meta:
        model = Produits
        fields = [
            'Produit', 'Type', 'PrixU', 'Quantitee', 'PrixT'
        ]

        widgets = {
            'Produit': forms.Select(attrs={
                'class': 'form-control', 'id': 'Produit'
            }),
            'Type': forms.Select(attrs={
                'class': 'form-control', 'id': 'Type'
            }),
    
            'PrixU': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'PrixU'
            }),
            'Quantitee': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Quantitee'
            }),
            
            'PrixT': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'PrixT'
            }),
            
            
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = [
            'Produit', 'Type', 'PrixU', 'Quantitee', 'PrixT'
        ]

        widgets = {
            'Produit': forms.Select(attrs={
                'class': 'form-control', 'id': 'Produit'
            }),
            'Type': forms.Select(attrs={
                'class': 'form-control', 'id': 'Type'
            }),
    
            'PrixU': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'PrixU'
            }),
            'Quantitee': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Quantitee'
            }),
            
            'PrixT': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'PrixT'
            }),
            
            
        }