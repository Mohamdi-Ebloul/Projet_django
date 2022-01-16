from django.contrib import admin

from Stock.models import Produits, Vente

# Register your models here.

admin.site.register(Produits)
admin.site.register(Vente)