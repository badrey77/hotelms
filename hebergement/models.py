from django.db import models
from django.db.models import CharField

STATUT_RESERVATION = (
    ('B', 'Brouillon'),
    ('C', 'Confirmée'),
    ('I', 'Check-in'),
    ('O', 'Check-out'),
)


class Reservation(models.Model):
    id = CharField(max_length=1000, verbose_name='ID de réservation')
    statut = CharField(max_length=1, choices=STATUT_RESERVATION, default='B')
