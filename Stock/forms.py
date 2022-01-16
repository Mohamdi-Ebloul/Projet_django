from django import forms
from django.forms.widgets import Widget

class PEnregistrer(forms.Form):
    Produit=forms.CharField(required=True,widget=forms.TextInput())
    Type=forms.CharField(required=True,widget=forms.TextInput())
    PrixU=forms.CharField(required=True,widget=forms.TextInput())
    Quantitee=forms.CharField(required=True,widget=forms.TextInput())
    PrixT=forms.CharField(required=True,widget=forms.TextInput())

'''''
class VEnregistrer(forms.Form):
    Produit=forms.CharField(required=True,widget=forms.TextInput())
    Type=forms.CharField(required=True,widget=forms.TextInput())
    PrixU=forms.CharField(required=True,widget=forms.TextInput())
    Quantitee=forms.CharField(required=True,widget=forms.TextInput())
    PrixT=forms.CharField(required=True,widget=forms.TextInput())
    date=forms.CharField(required=True,widget=forms.TextInput())
'''''
from .models import Produits, Vente


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
            'Type': forms.TextInput(attrs={
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