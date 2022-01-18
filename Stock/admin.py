from django.contrib import admin

from Stock.models import Produits, Vente,Marque,Libelle

# Register your models here.

admin.site.register(Produits)
admin.site.register(Vente)
admin.site.register(Marque)
admin.site.register(Libelle)