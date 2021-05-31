from django.forms import ModelForm
from .models import Produit, Commande
class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
    #fields=['libelle','description'] #pour quelques champs
class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = ['totalCde','produit']