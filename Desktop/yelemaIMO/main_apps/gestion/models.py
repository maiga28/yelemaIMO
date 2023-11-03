from django.db import models

# Create your models here.
class Proprietaire(models.Model):
    name = models.CharField(max_length=45)
    s_name = models.CharField(max_length=45)
    adresse = models.CharField(max_length=30)
    numero_telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.s_name}"
    
class Propriete(models.Model):
    titre = models.CharField(max_length=45)
    adresse = models.TextField(max_length=30)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=[('indisponible', 'Indisponible'),('disponible', 'Disponible'), ('loue', 'Loué'), ('vente', 'En vente')])
    type_propriete = models.CharField(max_length=20, choices=[('appartement', 'Appartement'), ('maison', 'Maison'), ('terrain', 'Terrain'), ('autre', 'Autre')])
    nombre_chambres = models.PositiveIntegerField()
    nombre_salles_bains = models.PositiveIntegerField()
    surface_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.titre

class Caracteristique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='caracteristiques/', blank=True, null=True)
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE)


    def __str__(self):
        return self.name