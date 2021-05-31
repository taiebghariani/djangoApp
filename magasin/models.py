from django.db import models


# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES= [('em', 'emballé'), ('fr', 'frais'), ('cs', 'conserver')]
    libelle = models.CharField(max_length=100)
    description = models.TextField(default="nom definie")
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES,default="em")
    img = models.ImageField(blank=True)
    emballage= models.OneToOneField('Emballage',on_delete=models.CASCADE,null=True)                                                          
    frs = models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    
    def __str__(self) :
        return f"{self.libelle},{self.description},{self.prix},{self.type},{self.emballage},{self.frs}"

class Emballage(models.Model):
    COUL_CHOICES=[ 
        ('bl','blanc'),
        ('rg','rouge'), 
        ('ble','bleu'),
        ('vr','vert'),
        ('muli','multicolore')
        ]
    matiere= models.CharField(max_length=100)
    couleur = models.CharField(max_length=10,default='Transparent', choices=COUL_CHOICES)
    def __str__(self) :
        return f"{self.matiere},{self.couleur}"

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    def __str__(self) :
        return f"{self.nom},{self.adresse}, {self.email},{self.telephone}"

class ProduitNC(Produit):
    duree_garantie=models.CharField(max_length=100)
    def __str__(self) :
        return f"ProduitNC: duree garantie: {self.duree_garantie}"

from datetime import date
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produit = models.ManyToManyField('Produit')
    def __str__(self):
        return f"commande : {self.produit}, {self.dateCde}, {self.totalCde} " 