"""
URL configuration for projet_django_dalla_costa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from gestion_materiel import views
from gestion_materiel.views import accueil, liste_enseignants, ajout_enseignant, liste_salles, liste_accessoires, ajout_salle, liste_materiels

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_materiel/accueil', accueil, name='accueil'),

    path('gestion_materiel/enseignant/liste_enseignants', liste_enseignants, name='liste_enseignants'),
    path('gestion_materiel/enseignant/ajout_enseignant', ajout_enseignant, name='ajout_enseignant'),
    path('gestion_materiel/enseignant/<int:enseignant_id>/supprimer', views.supprimer_enseignant, name='supprimer_enseignant'),

    path('gestion_materiel/salle/liste_salles', liste_salles, name='liste_salles'),
    path('gestion_materiel/salle/ajout_salle', ajout_salle, name='ajout_salle'),
    path('gestion_materiel/salle/supprimer/<int:salle_id>/', views.supprimer_salle, name='supprimer_salle'),

    path('gestion_materiel/materiel/liste_materiels', liste_materiels, name='liste_materiels'),

    path('gestion_materiel/materiel/<int:materiel_id>/accessoires/', liste_accessoires, name='liste_accessoires'),

    path('gestion_materiel/transferts/liste_transferts', views.liste_transferts, name='liste_transferts'),
]

