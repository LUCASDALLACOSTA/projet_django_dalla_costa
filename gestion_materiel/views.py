from django.shortcuts import render
from .models import Enseignant


def accueil(request):
    return render(request, 'gestion_materiel/accueil.html')

def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'gestion_materiel/enseignant/liste_enseignants.html', {'enseignants': enseignants})

