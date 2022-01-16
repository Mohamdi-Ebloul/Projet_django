from django.shortcuts import render
from django.http import HttpResponse
from Stock import models 
from Stock import forms
from .models import Vente
from .models import (
    Vente  
)
from .forms import (
    
    OrderForm,
    
)
# Create your views here.


def Produits(request):
    produit=models.Produits.objects.filter()
    context={
        'produits':produit
    }
    return render(request,'Pages/produits.html',context)


def Ventes(request):
    vente=models.Vente.objects.filter()
    context={
        'vente':vente
    }
    return render(request,'Pages/ventes.html',context)

def AjP(request):
    data=forms.PEnregistrer(request.POST or None)
    msg=''
    if data.is_valid():
        produit=models.Produits()
        produit.Produit=data.cleaned_data['Produit']
        produit.Type=data.cleaned_data['Type']
        produit.PrixU=data.cleaned_data['PrixU']
        produit.Quantitee=data.cleaned_data['Quantitee']
        produit.PrixT=data.cleaned_data['PrixT']
        produit.save()
        msg='Produit Enreistrer'

    context={
        'FEnregistrer':data,
        'msg':msg
    }
    return render(request,'Pages/AjP.html',context)





def AjV(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            Produit = forms.cleaned_data['Produit']
            Type = forms.cleaned_data['Type']
            PrixU = forms.cleaned_data['PrixU']
            Quantitee = forms.cleaned_data['Quantitee']
            PrixT = forms.cleaned_data['PrixT']
           
            Vente.objects.create(
                Produit=Produit,
                Type=Type,
                PrixU=PrixU,
                Quantitee=Quantitee,
                PrixT=PrixT,
            )
    context = {
        'form': forms
    }
    return render(request,'Pages/AjV.html',context)













'''
def Vente(request,Id_Produit):
    vente=models.Vente.objects.filter(Id_Produit=Id_Produit)
    context={
        'vente':vente
    }
    return render(request,'Pages/ventes.html',context)

'''


'''

def AjV(request):
    
    data=forms.VEnregistrer(request.POST or None)
    
    msg=''
    if data.is_valid():
        vente=models.Vente()
        
        vente.Produit=data.cleaned_data['Produit']
       
        vente.Type=data.cleaned_data['Type']
        vente.PrixU=data.cleaned_data['PrixU']
        vente.Quantitee=data.cleaned_data['Quantitee']
        vente.PrixT=data.cleaned_data['PrixT']
        vente.date=data.cleaned_data['date']
        vente.save()
        msg='Vente Enreistrer'

    context={
        'VEnregistrer':data,
        'msg':msg
    }
    return render(request,'Pages/AjV.html',context)

'''