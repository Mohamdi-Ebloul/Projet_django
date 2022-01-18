from django.shortcuts import render

from Stock.models import Produits, Vente


def Index(request):
    total_Produits = Produits.objects.count()
    total_Vente = Vente.objects.count()
    
    context = {
        'Produits': total_Produits,
        'Vente': total_Vente,
        
                  }
    return render(request,'index.html',context)
    
