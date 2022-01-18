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
from Stock.views import  Produitss, Ventes, AjP,AjV,AjL,AjM,Libelles,Marques,delv,delm,delp,dell
from .views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produits/',Produitss,name='produits'),
    path('',Index,name='dashboard'),
    path('delv/<id>/',delv,name='delv'),
    path('dell/<id>/',dell,name='dell'),
    path('delm/<id>/',delm,name='delm'),
    path('delp/<id>/',delp,name='delp'),
    path('vente/',Ventes,name='vente'),
    path('ajp/',AjP,name='ajp'),
    path('AjV/',AjV,name='AjV'),
    path('ajl/',AjL,name='ajl'),
    path('ajm/',AjM,name='ajm'),
    path('Marque/',Marques,name='Marque'),
    path('Libelle/',Libelles,name='Libelle'),


]
