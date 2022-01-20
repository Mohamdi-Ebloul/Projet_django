from django import forms
from django.forms.widgets import Widget

from .models import Service, StockEn,Sorti,Fournisseur,STOCK


class FEnregistrer(forms.ModelForm):
     class Meta:
        model = Fournisseur
        fields = [
            'Nom'
        ]

        widgets = {
            'Nom': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Nom'
            }),     
            
        }

class SEnregistrer(forms.ModelForm):
     class Meta:
        model = Service
        fields = [
            'Nom'
        ]

        widgets = {
            'Nom': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Nom'
            }),     
            
        }



class PEnregistrer(forms.ModelForm):
    class Meta:
        model = StockEn
        fields = [
            'QTEn', 'Fournisseur'
        ]

        widgets = {
            
            
            'QTEn': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEn'
            }),
           
           
            'Fournisseur': forms.Select(attrs={
                'class': 'form-control', 'id': 'Fournisseur'
            }),
            
            
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Sorti
        fields = [
             'Service',  'QTS'
        ]

        widgets = {
            
            'Service': forms.Select(attrs={
                'class': 'form-control', 'id': 'Service'
            }),
    
            'QTS': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTS'
            }),
           
            
            
        }

class StockEr(forms.ModelForm):
    class Meta:
        model = STOCK
        fields = [
            'Designation', 'QTEx', 'QTEn','QTS','QTR'
        ]

        widgets = {
            'Designation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Designation'
            }),
            
            'QTEx': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEx'
            }),
            'QTEn': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEn'
            }),
           'QTS': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEn'
            }),
            'QTR': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTR'
            }),
            
            
            
        }
class SE(forms.ModelForm):
    class Meta:
        model = STOCK
        fields = [
            'Designation'
        ]

        widgets = {
            'Designation': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'Designation'
            }),
        }


class Sr(forms.ModelForm):
    class Meta:
        model = STOCK
        fields = [
            'QTEx', 'QTEn','QTR'
        ]

        widgets = {
           
            
            'QTEx': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEx'
            }),
            'QTEn': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTEn'
            }),
            'QTR': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'QTR'
            }),
            
        }