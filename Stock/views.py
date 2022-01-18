from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from Stock import models 

from .models import (
    Libelle, Marque, Vente ,Produits,
)
from .forms import (
    
    OrderForm,PEnregistrer,MEnregistrer,LEnregistrer
    
)
# Create your views here.

def AjP(request):
    forms = PEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = PEnregistrer(request.POST)
        if forms.is_valid():
           Produit=forms.cleaned_data['Produit']
           Type=forms.cleaned_data['Type']
           PrixU=forms.cleaned_data['PrixU']
           Quantitee=forms.cleaned_data['Quantitee']
           PrixT=forms.cleaned_data['PrixT']
           
           msg='Produit Enreistrer'
           Produits.objects.create(
                Produit=Produit,
                Type=Type,
                PrixU=PrixU,
                Quantitee=Quantitee,
                PrixT=PrixT,
            )
    context={
        'form':forms,
        'msg':msg
    }
    return render(request,'Pages/AjP.html',context)

def Produitss(request):
    produit=models.Produits.objects.filter()
    context={
        'produits':produit
    }
    return render(request,'Pages/produits.html',context)

def delp(request,id):
    delp=Produits.objects.get(id=id)
    delp.delete()
    return redirect('produits')



def AjV(request):
    forms = OrderForm()
    msg=''
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            Produit = forms.cleaned_data['Produit']
            Type = forms.cleaned_data['Type']
            PrixU = forms.cleaned_data['PrixU']
            Quantitee = forms.cleaned_data['Quantitee']
            PrixT = forms.cleaned_data['PrixT']
            msg='Vente Ajouter'
            Vente.objects.create(
                Produit=Produit,
                Type=Type,
                PrixU=PrixU,
                Quantitee=Quantitee,
                PrixT=PrixT,
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjV.html',context)

def Ventes(request):
    vente=models.Vente.objects.filter()
    context={
        'vente':vente
    }
    return render(request,'Pages/ventes.html',context)

def delv(request,id):
    delv=Vente.objects.get(id=id)
    delv.delete()
    return redirect('vente')




def AjM(request):
    forms = MEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = MEnregistrer(request.POST)
        if forms.is_valid():
            Type = forms.cleaned_data['Type']
            msg=' Marque Enregister'
            Marque.objects.create(
                Type=Type
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjM.html',context)

def Marques(request):
    Marque=models.Marque.objects.filter()
    context={
        'Marque':Marque
    }
    return render(request,'Pages/Marque.html',context)

def delm(request,id):
    delm=Marque.objects.get(id=id)
    delm.delete()
    return redirect('Marque')



def AjL(request):
    forms = LEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = LEnregistrer(request.POST)
        if forms.is_valid():     
            Produit = forms.cleaned_data['Produit']
            msg='Produit Enregister'          
            Libelle.objects.create(             
                Produit=Produit,
               
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjL.html',context)


def Libelles(request):
    Libelle=models.Libelle.objects.filter()
    context={
        'Libelle':Libelle
    }
    return render(request,'Pages/Libelle.html',context)

def dell(request,id):
    dell=Libelle.objects.get(id=id)
    dell.delete()
    return redirect('Libelle')








