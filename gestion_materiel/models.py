from django.db import models
from django.urls import reverse

class Enseignant(models.Model):
    nom = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )
    prenom = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )

class Salle(models.Model):
    nom = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )
    etage = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='aucun'
    )

    def get_delete_url(self):
        return reverse('supprimer_salle', kwargs={'salle_id': self.id})


class Materiel(models.Model):
    nom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default='aucun'
    )
    budget = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default='aucun'
    )
    proprietaire = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='materiels_possedes'  # Accesseur inverse unique pour la relation ForeignKey proprietaire
    )
    lieu = models.ForeignKey(
        Salle,
        on_delete=models.CASCADE,
        null=True
    )
    possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='materiels_en_possession'  # Accesseur inverse unique pour la relation ForeignKey possesseur
    )

    def get_accessoires_url(self):
        return reverse('liste_accessoires', args=[self.id])

class TransfertMateriel(models.Model):
    material = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,
        null=True
    )
    ancien_possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='transferts_sortants'  # Accesseur inverse unique pour la relation ForeignKey ancien_possesseur
    )
    nouveau_possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='transferts_entrants'  # Accesseur inverse unique pour la relation ForeignKey nouveau_possesseur
    )
    date_transfert = models.DateField()
    lieu_transfer = models.CharField(
        max_length=100
    )
    occasion = models.CharField(
        max_length=100
    )
    objectif = models.TextField()

class AccessoireMateriel(models.Model):
    material = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,
        null=True
    )
    nom = models.CharField(
        max_length=100
    )
    present = models.BooleanField(
        default=True
    )
    etat = models.CharField(max_length=100)
