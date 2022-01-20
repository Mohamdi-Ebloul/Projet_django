from django.contrib import admin

from Stock.models import StockEn, Sorti,Service,Fournisseur,STOCK

# Register your models here.

admin.site.register(StockEn)
admin.site.register(Sorti)
admin.site.register(Service)
admin.site.register(Fournisseur)
admin.site.register(STOCK)