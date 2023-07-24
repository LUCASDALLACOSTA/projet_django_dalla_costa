from django import forms
from .models import Enseignant, Salle


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']

class SalleForm(forms.ModelForm):
    ETAGE_CHOICES = (
        ('rez-de-chaussee', 'Rez-de-chaussée'),
        ('1er', '1er étage'),
        ('2e', '2eme étage'),
        ('3e', '3eme étage'),

    )

    etage = forms.ChoiceField(choices=ETAGE_CHOICES)

    class Meta:
        model = Salle
        fields = ['nom', 'etage']