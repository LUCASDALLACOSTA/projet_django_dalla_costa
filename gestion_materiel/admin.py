from django.contrib import admin

# Register your models here.
from .models import Enseignant,Salle,Materiel,TransfertMateriel,AccessoireMateriel

admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(TransfertMateriel)
admin.site.register(AccessoireMateriel)