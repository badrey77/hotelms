from django.contrib import admin
from django.contrib.admin import ModelAdmin

from hebergement.models import Reservation, Chambre


@admin.register(Reservation)
class ReservationConfig(ModelAdmin):
    list_display = ['num', 'demandeur','date_commande','statut']
    filter_horizontal = ['services_inclus']
    raw_id_fields = ['demandeur']
    search_fields = ['num', 'demandeur']
    list_filter = ['date_commande','statut']
    # fieldsets = {
    #     (None, { 'fields' : ('num', 'status', 'classe',)},
    # ),
    # }

@admin.register(Chambre)
class ChambreConfig(ModelAdmin):
    list_display = ['num', 'type_chambre', 'statut']