import datetime
from datetime import timedelta

from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline

from hebergement.models import Reservation, Chambre, Agent, ReservationChambre, ReservationSalle, Salle, STATUS_CHAMBRE, \
    Section


@admin.register(Agent)
class AgentConfig(ModelAdmin):
    list_display = ['nom', 'prenom', 'contact', 'reference']


@admin.register(Chambre)
class ChambreConfig(ModelAdmin):
    list_display = ['num', 'type_chambre', 'status']
    search_fields = ['num']
    list_filter = ['section', 'type_chambre', 'status']

    def get_readonly_fields(self, request, obj=None):
        rof = []
        for i in range(7):
            day = datetime.date.today() + timedelta(days=i)

            res = ReservationChambre.objects.filter(chambre_id=obj.id,
                                                       date_checkin__lte=day,
                                                       date_checkout__gt=day)

            if res.count() > 0:
                print(res)
                foo = lambda self: res.first().reservation.status
            else:
                print('L')
                foo = lambda self: 'L'

            foo.short_description = (day.strftime('%A'))
            rof.append(foo.short_description)
            setattr(self, foo.short_description, foo)
        return rof


@admin.register(Section)
class SectionConfig(ModelAdmin):
    list_display = ['designation']
    search_fields = ['designation']


@admin.register(Salle)
class SalleConfig(ModelAdmin):
    list_display = ['designation', 'type_salle', 'status']
    search_fields = ['designation']


class ReservationChambreInline(StackedInline):
    model = ReservationChambre
    extra = 0
    autocomplete_fields = ["chambre", "personnes"]


class ReservationSalleInline(TabularInline):
    model = ReservationSalle
    extra = 0
    autocomplete_fields = ["salle"]


@admin.register(Reservation)
class ReservationConfig(ModelAdmin):
    list_display = ['num', 'demandeur','date_commande','status']
    filter_horizontal = ['services_inclus','personnes']
    autocomplete_fields = ['demandeur']
    search_fields = ['num', 'demandeur']
    list_filter = ['date_commande','status']
    fieldsets = (
        (None, {
            'fields': (('num','status', 'classe'),)
        }),
        ('Au profit de', {
            'fields': (('demandeur', 'nbr_adultes', 'nbr_enfants', 'personnes'),)
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

    def changelist_view(self, request, extra_context=None):
        jours = [datetime.date.today() + timedelta(days=x) for x in range(30)]
        chambres = []
        for ch in Chambre.objects.all():
            ch.jours = ch.reservations()
            chambres.append(ch)
        extra_context = {
            'app_list': [
                { 'name' : 'Hebergement'},
            ],
            'chambres' : chambres,
            'jours' : jours
        }
        return super().changelist_view(request, extra_context)

    class Media:
        js = [
            'js/jquery-ui.min.js',
            'js/reservation.js'
        ]
        css = {
            "all": ['css/jquery-ui.min.css'],
        }
