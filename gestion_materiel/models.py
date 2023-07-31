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

    def __str__(self):
        return f"{self.nom} {self.prenom}"

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

    def __str__(self):
        if self.etage.lower() == "rez-de-chaussée":
            return f"{self.nom} ({self.etage})"
        else:
            return f"{self.nom} ({self.etage} Étage)"

    def get_delete_url(self):
        return reverse('supprimer_salle', kwargs={'salle_id': self.id})


class Materiel(models.Model):
    nom = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default=''
    )
    budget = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default=''
    )
    proprietaire = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='materiels_possedes'
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
        blank=True,
        related_name='materiels_en_possession'
    )

    def __str__(self):
        return self.nom

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
        related_name='transferts_sortants'
    )
    nouveau_possesseur = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,
        null=True,
        related_name='transferts_entrants'
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
        max_length=100,
        blank = True
    )
    present = models.BooleanField(
        default=True
    )
    etat = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

