from django.contrib import admin

# Register your models here.
from .models import Enseignant,Salle,Materiel,TransfertMateriel,AccessoireMateriel

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom")

admin.site.register(Enseignant,EnseignantAdmin)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(TransfertMateriel)
admin.site.register(AccessoireMateriel)