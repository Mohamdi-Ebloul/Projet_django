"""Gestion_stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Stock.views import  ( Stocks, Sortis, StocknktEntrer,StocknktSortie,
                          AjoutFournisseur,AjouteService,Fournisseurs,Services,
                             delSortie,delService,delStock,delFournisseur,STOCKS,AjoutDesignation ,
                             AjouterUtilisateur,UtilisateursListView,
                             
                             )
from .views import Aceeil
from .views import login_page, logout_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Stocks/',Stocks,name='Stocks'),
    path('',Aceeil,name='Acceil'),
    path('delSortie/<id>/',delSortie,name='delSortie'),
    path('delFournisseur/<id>/',delFournisseur,name='delFournisseur'),
    path('delService/<id>/',delService,name='delService'),
    path('delStock/<id>/',delStock,name='delStock'),
    path('sorti/',Sortis,name='sorti'),
    path('StocknktEntrer/<id>/',StocknktEntrer,name='StocknktEntrer'),
    path('StocknktSortie/<id>/',StocknktSortie,name='StocknktSortie'),
    path('AjoutFournisseur/',AjoutFournisseur,name='AjoutFournisseur'),
    path('AjouteService/',AjouteService,name='AjouteService'),
    path('Service/',Services,name='Service'),
    path('Fournisseur/',Fournisseurs,name='Fournisseur'),
    path('STOCKS/',STOCKS,name='STOCKS'),
    path('AjoutDesignation/',AjoutDesignation,name='AjoutDesignation'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('Utilisateur/', UtilisateursListView.as_view(), name='Utilisateur'),
    path('Ajouteuser/', AjouterUtilisateur, name='Ajouteuser'),



]
