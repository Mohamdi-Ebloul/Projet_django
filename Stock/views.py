from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from Stock import models 

from .models import (
    STOCK, Fournisseur, Service, Sorti ,StockEn,
)
from .forms import (
    
    OrderForm,PEnregistrer,SEnregistrer,FEnregistrer,StockEr,SE,Sr
    
)
# Create your views here.

def AjP(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = PEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = PEnregistrer(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           QTEx=STOCK.objects.get(id=id).QTEx
           QTEn=forms.cleaned_data['QTEn']         
           QTR=STOCK.objects.get(id=id).QTEx+QTEn
           Fournisseur=forms.cleaned_data['Fournisseur']
           
           msg='Stock Enreistrer'
           StockEn.objects.create(
                Designation=Designation,
                QTEx=QTEx,
                QTEn=QTEn,
                QTR=QTR,
                Fournisseur=Fournisseur,

            )

        d=STOCK.objects.get(id=id).Designation
        q1=STOCK.objects.get(id=id).QTEx+forms.cleaned_data['QTEn'] 
        q2=STOCK.objects.get(id=id).QTEn+forms.cleaned_data['QTEn']        
        q3=STOCK.objects.get(id=id).QTS
        q4=STOCK.objects.get(id=id).QTR+forms.cleaned_data['QTEn'] 
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1,QTEn=q2,QTS=q3,QTR=q4)
           
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg
    }
 
    return render(request,'Pages/AjP.html',context)

def Stocks(request):
    produit=models.StockEn.objects.filter()
    context={
        'Stock':produit
    }
    return render(request,'Pages/Stock.html',context)

def delp(request,id):
    delp=StockEn.objects.get(id=id)
    delp.delete()
    return redirect('Stocks')



def AjV(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = OrderForm()
    msg=''
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           QTEx=STOCK.objects.get(id=id).QTEx
           QTS=forms.cleaned_data['QTS']         
           QTR=QTEx-QTS
           Service=forms.cleaned_data['Service']
           
           msg='Stock Enreistrer Sortie'
           Sorti.objects.create(
                Designation=Designation,
                QTEx=QTEx,
                QTS=QTS,
                QTR=QTR,
                Service=Service,

            )
        d=STOCK.objects.get(id=id).Designation
        q1=STOCK.objects.get(id=id).QTEx-forms.cleaned_data['QTS'] 
        q2=STOCK.objects.get(id=id).QTEn        
        q3=STOCK.objects.get(id=id).QTS+forms.cleaned_data['QTS'] 
        q4=STOCK.objects.get(id=id).QTR-forms.cleaned_data['QTS'] 
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1,QTEn=q2,QTS=q3,QTR=q4)
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg
    }
    return render(request,'Pages/AjV.html',context)

def Sortis(request):
    sorti=models.Sorti.objects.filter()
    context={
        'sorti':sorti
    }
    return render(request,'Pages/sortis.html',context)

def delv(request,id):
    delv=Sorti.objects.get(id=id)
    delv.delete()
    return redirect('sorti')




def AjM(request):
    forms = SEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = SEnregistrer(request.POST)
        if forms.is_valid():
            Nom = forms.cleaned_data['Nom']
            msg=' Service Enregister'
            Service.objects.create(
                Nom=Nom
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjM.html',context)

def Services(request):
    Service=models.Service.objects.filter()
    context={
        'Service':Service
    }
    return render(request,'Pages/Service.html',context)

def delm(request,id):
    delm=Service.objects.get(id=id)
    delm.delete()
    return redirect('Service')



def AjL(request):
    forms = FEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = FEnregistrer(request.POST)
        if forms.is_valid():     
            Nom = forms.cleaned_data['Nom']
            msg='Produit Enregister'          
            Fournisseur.objects.create(             
                Nom=Nom,
               
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjL.html',context)


def Fournisseurs(request):
    Fournisseur=models.Fournisseur.objects.filter()
    context={
        'Fournisseur':Fournisseur
    }
    return render(request,'Pages/Fournisseur.html',context)

def dell(request,id):
    dell=Fournisseur.objects.get(id=id)
    dell.delete()
    return redirect('Fournisseur')



def STOCKS(request):
    STOCK1=models.STOCK.objects.filter()
    context={
        'STOCK1':STOCK1
    }
    return render(request,'Pages/STOCKS.html',context)


def AJS(request):
    forms = SE()
    msg=''
    if request.method == 'POST':
        forms = SE(request.POST)
        if forms.is_valid():     
            Designation= forms.cleaned_data['Designation']
            msg='Designation Enregister'          
            STOCK.objects.create(             
                Designation=Designation,
               
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AJS.html',context)


