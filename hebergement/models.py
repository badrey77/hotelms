
from django.utils import timezone

from django.db import models
from django.db.models import CharField, IntegerField, PositiveSmallIntegerField, DateField, ForeignKey, CASCADE, \
    TextField, BooleanField, DateTimeField, ManyToManyField

from core.models import Personne, Service, Classe

STATUT_RESERVATION = (
    ('B', 'Brouillon'),
    ('C', 'Confirmée'),
    ('T', 'Terminée'),
    ('O', 'Check-out'),
)

SOURCES_RESERVATION = (
    ('S', 'Sur Site'),
    ('W', 'Le Site Web'),
    ('A', 'Une Agence'),
    ('O', 'Autres'),
)


class Agent(Personne):
    reference = CharField(max_length=1000, verbose_name='référence')
    contact = CharField(max_length=1000, verbose_name='contact')

    def __str__(self):
        return f'{self.contact} ({self.reference})' if self is not None else ''


class Reservation(models.Model):
    num = CharField(max_length=1000, verbose_name='ID de réservation')
    statut = CharField(max_length=1, choices=STATUT_RESERVATION, default='B')
    classe = ForeignKey(Classe, on_delete=CASCADE)
    demandeur = ForeignKey(Personne, on_delete=CASCADE, related_name='reservations', verbose_name='demandeur de réservation')
    nbr_adultes = PositiveSmallIntegerField(verbose_name="nombre d'adultes")
    nbr_enfants = PositiveSmallIntegerField(verbose_name="nombre d'enfants")
    date_commande = DateField(default=timezone.now(), verbose_name='date de la commande')
    services_inclus = ManyToManyField(Service, verbose_name='services inclus')
    a_travers = CharField(max_length=1, choices=SOURCES_RESERVATION, default='S')
    agent = ForeignKey(Agent, on_delete=CASCADE, null=True, blank=True, related_name='reservations_effectuees')
    notes = TextField(null=True, blank=True)
    pickup = BooleanField(default=False,verbose_name='nécessite un transfert (pickup)?')

    def __str__(self):
        return f'{self.num}' if self is not None else ''



TYPE_CHAMBRE = (
    ('IDV', 'Individuelle (1 lit)'),
    ('DXL', 'Double (2 lits)'),
    ('DLS', 'Double (2 lits séparés)'),
    ('SUT', 'Suite'),
)

STATUT_CHAMBRE = (
    ('L', 'Libre'),
    ('B', 'Reservation Brouillon'),
    ('C', 'Reservation Confirmée'),
    ('T', 'Reservation Terminée'),
    ('O', 'Check-out'),
)

class Chambre(Service):
    num = CharField(max_length=25, verbose_name="numéro de chambre")
    type_chambre = CharField(max_length=3, choices=TYPE_CHAMBRE, verbose_name='type de chambre')
    info_sup = TextField(blank=True, null=True, verbose_name='Informations Supplémentaires')
    statut = CharField(max_length=1, choices=STATUT_CHAMBRE, default='L')

    def __str__(self):
        return f'Chambre n° {self.num}' if self is not None else ''

    def save(self, *args, **kwargs):
        self.type = 'HBG'
        super().save(*args, **kwargs)


class ReservationChambre(models.Model):
    reservation = ForeignKey(Reservation, on_delete=CASCADE, verbose_name='réservation')
    chambre = ForeignKey(Chambre, on_delete=CASCADE, verbose_name='chambre')
    date_checkin = DateField(null=True, blank=True, verbose_name='Date de check-in')
    date_checkout = DateField(null=True, blank=True, verbose_name='Date de check-out')

    def __str__(self):
        return f'Réservation {self.reservation} pour {self.chambre}' if self is not None else ''


TYPE_SALLE = (
    ('CFR', 'Conférences'),
    ('FET', 'Fêtes'),
    ('AUD', 'Auditorium'),
)


class Salle(models.Model):
    designation = CharField(max_length=25, verbose_name="désignation de la salle")
    type_salle = CharField(max_length=3, choices=TYPE_SALLE, verbose_name='type de salle')
    info_sup = TextField(blank=True, null=True, verbose_name='Informations Supplémentaires')

    def __str__(self):
        return f'Salle {self.designation}' if self is not None else ''


class ReservationSalle(models.Model):
    reservation = ForeignKey(Reservation, on_delete=CASCADE, verbose_name='réservation')
    salle = ForeignKey(Chambre, on_delete=CASCADE, verbose_name='salle')
    date_debut = DateTimeField(verbose_name='Date de debut')
    date_fin = DateTimeField(verbose_name='Date de fin')

    def __str__(self):
        return f'Réservation {self.reservation} pour {self.salle} de {self.date_debut} à {self.fin}' if self is not None else ''