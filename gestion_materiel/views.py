from django.shortcuts import render, redirect, get_object_or_404
from .models import Enseignant, Materiel, AccessoireMateriel, TransfertMateriel, Salle
from .forms import EnseignantForm, SalleForm
from django.contrib import messages

def accueil(request):
    return render(request, 'gestion_materiel/accueil.html')

"""enseignant"""
def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'gestion_materiel/enseignant/liste_enseignants.html', {'enseignants': enseignants})

def ajout_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enseignant ajouté avec succès')
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'gestion_materiel/enseignant/ajout_enseignant.html', {'form': form})

def supprimer_enseignant(request, enseignant_id):
    if request.method == 'POST':
        enseignant = Enseignant.objects.get(id=enseignant_id)
        enseignant.delete()
        messages.add_message(request, messages.SUCCESS, "L'enseignant a été supprimé avec succès", extra_tags='danger')
    return redirect('liste_enseignants')

"""salle"""
def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'gestion_materiel/salle/liste_salles.html', {'salles': salles})

def liste_materiels_salle(request, salle_id):
    salle = get_object_or_404(Salle, id=salle_id)
    materiels = Materiel.objects.filter(lieu=salle)
    return render(request, 'gestion_materiel/salle/liste_materiels_salle.html', {'salle': salle, 'materiels': materiels})

def ajout_salle(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salle ajoutée avec succès')
            return redirect('liste_salles')
    else:
        form = SalleForm()
    return render(request, 'gestion_materiel/salle/ajout_salle.html', {'form': form})

def supprimer_salle(request, salle_id):
    salle = get_object_or_404(Salle, id=salle_id)
    salle.delete()
    messages.add_message(request, messages.SUCCESS, "La salle a été supprimée avec succès", extra_tags='danger')
    return redirect('liste_salles')


def liste_accessoires(request, materiel_id):
    materiel = Materiel.objects.get(id=materiel_id)
    accessoires = AccessoireMateriel.objects.filter(material=materiel)
    return render(request, 'gestion_materiel/materiel/liste_accessoires.html', {'materiel': materiel, 'accessoires': accessoires})

def liste_transferts(request):
    transferts = TransfertMateriel.objects.all()
    return render(request, 'gestion_materiel/transferts/liste_transferts.html', {'transferts': transferts})

"""materiel"""
def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'gestion_materiel/materiel/liste_materiels.html', {'materiels': materiels})

def supprimer_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    materiel.delete()
    messages.add_message(request, messages.SUCCESS, "Le matériel a été supprimé avec succès", extra_tags='danger')
    return redirect('liste_materiels')
