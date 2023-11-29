from django.db import models
import random
from string import ascii_lowercase as lets

# Create your models here.
class Proprietaire(models.Model):
    
    name = models.CharField(max_length=45)
    s_name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='image/')
    adresse = models.CharField(max_length=30)
    numero_telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.s_name}"

class ProprieteManager(models.Manager):
    
    def disponible(self):
        return self.get_queryset().filter(statut='disponible')
    
    def indisponible(self):
        return self.get_queryset().filter(statut='indisponible')
    
    def create_dummy(self):
        titre = 'Dummy:' + ''.join(random.choice(lets) for _ in range(10))
        adresse = 'Dummy:' + ''.join(random.choice(lets) for _ in range(10))
        description = ''.join(random.choice(lets) for _ in range(100))
        statut = random.choice(['disponible', 'indisponible'])
        type_propriete = random.choice(['appartement', 'maison', 'terrain', 'autre'])
        nombre_chambres = random.randint(1, 10)
        nombre_salles_bains = random.randint(1, 10)
        surface_m2 = round(random.uniform(1, 100), 2)
        
        return self.create(
            titre=titre,
            adresse=adresse,
            description=description,
            statut=statut,
            type_propriete=type_propriete,
            nombre_chambres=nombre_chambres,
            nombre_salles_bains=nombre_salles_bains,
            surface_m2=surface_m2
        )

class Propriete(models.Model):
    titre = models.CharField(max_length=45)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    adresse = models.CharField(max_length=30)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=[('indisponible', 'Indisponible'),('disponible', 'Disponible'), ('loue', 'Loué'), ('vente', 'En vente')])
    type_propriete = models.CharField(max_length=20, choices=[('appartement', 'Appartement'), ('maison', 'Maison'), ('terrain', 'Terrain'), ('autre', 'Autre')])
    nombre_chambres = models.PositiveIntegerField()
    nombre_salles_bains = models.PositiveIntegerField()
    surface_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    
    objects = ProprieteManager()  # Ajout du manager à la classe Propriete
    
    def __str__(self):
        return self.titre
    
class Contrat_bail(models.Model):
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE, null=False,blank=True)
    debut = models.DateTimeField(auto_now_add=True)
    fin = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
