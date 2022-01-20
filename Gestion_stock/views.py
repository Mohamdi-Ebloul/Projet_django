from django.shortcuts import render

from Stock.models import StockEn, Sorti


def Index(request):
    total_Stock = StockEn.objects.count()
    total_Sorti = Sorti.objects.count()
    
    context = {
        'Stock': total_Stock,
        'Sorti': total_Sorti,
        
                  }
    return render(request,'index.html',context)
    
