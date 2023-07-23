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

from gestion_materiel.views import accueil, liste_enseignants, ajout_enseignant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion_materiel/accueil', accueil, name='accueil'),
    path('gestion_materiel/enseignant/liste_enseignants', liste_enseignants, name='liste_enseignants'),
    path('gestion_materiel/enseignant/ajout_enseignant', ajout_enseignant, name='ajout_enseignant'),
]

