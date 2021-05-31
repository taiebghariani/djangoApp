
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Produit, Commande
from .forms import ProduitForm, CommandeForm

# def index(request):
#     template=loader.get_template('mesProduits.html')
#     list= Produit.objects.all()
#     return HttpResponse(template.render( {'list':list} ))



def index(request):
    list=Produit.objects.all()
    return render(request,'vitrine.html',{'list':list})
    # if request.method == "POST":
    #     form = ProduitForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         """pdt = Produit()
    #         pdt.libelle = form.cleaned_data["libelle"]
    #         pdt.img= form.cleaned_data["img"]
    #         ...
    #         pdt.save()"""
    #         form.save()
    # else:
    #     form = ProduitForm()  # créer formulaire vide
    # return render(request, 'majProduits.html', {'form': form})
    # def commande (request):
    #         if request.method == "POST":
    #             commandeForm = CommandeForm(request.POST, request.FILES)
    #             if commandeForm.is_valid():
    #                 commande = Commande()
    #                 commande.produit = commandeForm.cleaned_data["produit"]
    #                 commande.totalCde= commandeForm.cleaned_data["totalCde"]
    #                 commande.save()
    #                 commandeForm.save()
    #         return render(request, 'commande.html', {'commandeForm': commandeForm})
    def comm(request) :
        HttpResponse('commande')




