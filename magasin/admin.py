from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Produit)
admin.site.register(Emballage)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
