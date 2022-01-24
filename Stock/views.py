from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from Stock import models 
from django.views.generic import ListView
from .models import (
    STOCK, Fournisseur, Service, Sorti ,StockEn,User,Utilisateurs
)
from .forms import (
    
    SortieEnregistrer,StockEnregistrer,SEnregistrer,FEnregistrer,EntrerEnregistrer,UtilisateurForm
    
)
# Create your views here.



@login_required(login_url='login')
def AjouterUtilisateur(request):
    forms = UtilisateurForm()
    if request.method == 'POST':
        forms = UtilisateurForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, Utilisateur=True
                )
                Utilisateurs.objects.create(user=user, name=name, address=address)
                return redirect('Utilisateur')
    context = {
        'form': forms
    }
    return render(request, 'Pages/Ajouteuser.html', context)


class UtilisateursListView(ListView):
    model = Utilisateurs
    template_name = 'Pages/Utilisateur.html'
    context_object_name = 'Utilisateur'




@login_required(login_url='login')
def StocknktEntrer(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = EntrerEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = EntrerEnregistrer(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           QTEx=STOCK.objects.get(id=id).QTEx
           QTEn=forms.cleaned_data['QTEn']         
           
           Fournisseur=forms.cleaned_data['Fournisseur']
           
           msg='Stock Enreistrer'
           StockEn.objects.create(
                Designation=Designation,
                QTEx=QTEx,
                QTEn=QTEn,
                Fournisseur=Fournisseur,

            )

        d=STOCK.objects.get(id=id).Designation
        q1=STOCK.objects.get(id=id).QTEx+forms.cleaned_data['QTEn']  
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1)
           
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg
    }
 
    return render(request,'Pages/StocknktEntrer.html',context)
@login_required(login_url='login')
def Stocks(request):
    produit=models.StockEn.objects.filter()
    context={
        'Stock':produit
    }
    return render(request,'Pages/Stock.html',context)

@login_required(login_url='login')
def delStock(request,id):
    delStock=StockEn.objects.get(id=id)
    delStock.delete()
    return redirect('Stocks')


@login_required(login_url='login')
def StocknktSortie(request,id):
    
    STOCK1=models.STOCK.objects.filter(id=id)
    forms = SortieEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = SortieEnregistrer(request.POST)
        if forms.is_valid():
           
           Designation=STOCK.objects.get(id=id)
           QTS=forms.cleaned_data['QTS']         
           QTR=STOCK.objects.get(id=id).QTEx-QTS
           Service=forms.cleaned_data['Service']
           
           msg='Stock Enreistrer Sortie'
           Sorti.objects.create(
                Designation=Designation,
                
                QTS=QTS,
                QTR=QTR,
                Service=Service,

            )
        d=STOCK.objects.get(id=id).Designation
        q1=STOCK.objects.get(id=id).QTEx-forms.cleaned_data['QTS'] 
        
        STOCK.objects.filter(id=id).update(Designation=d,QTEx=q1)
    context={
        'form':forms,'STOCK1':STOCK1,
        'msg':msg
    }
    return render(request,'Pages/StocknktSortie.html',context)

@login_required(login_url='login')
def Sortis(request):
    sorti=models.Sorti.objects.filter()
    context={
        'sorti':sorti
    }
    return render(request,'Pages/sortis.html',context)

@login_required(login_url='login')
def delSortie(request,id):
    delSortie=Sorti.objects.get(id=id)
    delSortie.delete()
    return redirect('sorti')



@login_required(login_url='login')
def AjouteService(request):
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
    return render(request,'Pages/AjouteService.html',context)

@login_required(login_url='login')
def Services(request):
    Service=models.Service.objects.filter()
    context={
        'Service':Service
    }
    return render(request,'Pages/Service.html',context)


@login_required(login_url='login')
def delService(request,id):
    delService=Service.objects.get(id=id)
    delService.delete()
    return redirect('Service')


@login_required(login_url='login')
def AjoutFournisseur(request):
    forms = FEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = FEnregistrer(request.POST)
        if forms.is_valid():     
            Nom = forms.cleaned_data['Nom']
            Abrevation = forms.cleaned_data['Abrevation']
            NomDirecteur = forms.cleaned_data['NomDirecteur']
            Nif = forms.cleaned_data['Nif']
            Tel = forms.cleaned_data['Tel']
            Email = forms.cleaned_data['Email']
            Domaine = forms.cleaned_data['Domaine']
            RC = forms.cleaned_data['RC']
            msg='Founiseur Ajouter'          
            Fournisseur.objects.create(             
                Nom=Nom,
                Abrevation=Abrevation,
                NomDirecteur=NomDirecteur,
                Nif=Nif,
                Tel=Tel,
                Email=Email,
                Domaine=Domaine,
                RC=RC,          
            )
    context = {
        'form': forms,
        'msg':msg
    }
    return render(request,'Pages/AjoutFournisseur.html',context)


@login_required(login_url='login')
def Fournisseurs(request):
    Fournisseur=models.Fournisseur.objects.filter()
    context={
        'Fournisseur':Fournisseur
    }
    return render(request,'Pages/Fournisseur.html',context)

@login_required(login_url='login')
def delFournisseur(request,id):
    delFournisseur=Fournisseur.objects.get(id=id)
    delFournisseur.delete()
    return redirect('Fournisseur')


@login_required(login_url='login')
def STOCKS(request):
    STOCK1=models.STOCK.objects.filter()
    context={
        'STOCK1':STOCK1
    }
    return render(request,'Pages/STOCKS.html',context)

@login_required(login_url='login')
def AjoutDesignation(request):
    forms = StockEnregistrer()
    msg=''
    if request.method == 'POST':
        forms = StockEnregistrer(request.POST)
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
    return render(request,'Pages/AjoutDesignation.html',context)


