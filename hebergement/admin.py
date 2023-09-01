from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from hebergement.models import Reservation, Chambre, Agent, ReservationChambre, ReservationSalle, Salle


@admin.register(Agent)
class AgentConfig(ModelAdmin):
    list_display = ['nom', 'prenom', 'contact', 'reference']


@admin.register(Chambre)
class ChambreConfig(ModelAdmin):
    list_display = ['num', 'type_chambre', 'statut']
    #fields = ['num', 'type_chambre', 'statut','info_sup']
    search_fields = ['num']


@admin.register(Salle)
class SalleConfig(ModelAdmin):
    list_display = ['designation', 'type_salle', 'statut']
    search_fields = ['designation']


class ReservationChambreInline(TabularInline):
    model = ReservationChambre
    extra = 0
    autocomplete_fields = ["chambre"]


class ReservationSalleInline(TabularInline):
    model = ReservationSalle
    extra = 0
    autocomplete_fields = ["salle"]


@admin.register(Reservation)
class ReservationConfig(ModelAdmin):
    list_display = ['num', 'demandeur','date_commande','statut']
    filter_horizontal = ['services_inclus']
    autocomplete_fields = ['demandeur']
    search_fields = ['num', 'demandeur']
    list_filter = ['date_commande','statut']
    fieldsets = (
        (None, {
            'fields': (('num','statut', 'classe'),)
        }),
        ('Au profit de', {
            'fields': (('demandeur', 'nbr_adultes', 'nbr_enfants'),)
        }),
        ('Informations Suplémentaires', {
            'fields': (('date_commande', 'a_travers', 'agent'),)
        }),
        ('Inclus', {
            'fields': ('services_inclus', 'notes',)
        }),
    )

    def get_inlines(self, request, obj):
        if obj == None:
            return []

        if obj.services_inclus.count() == 0:
            return []

        inline = []

        if obj.services_inclus.filter(designation__iexact='hébergement'):
            inline.append(ReservationChambreInline)

        if obj.services_inclus.filter(designation__iexact='accueil'):
            inline.append(ReservationSalleInline)
        return inline

    class Media:
        js = [
            'js/jquery-ui.min.js',
            'js/reservation.js'
        ]
        css = {
            "all": ['css/jquery-ui.min.css'],
        }
