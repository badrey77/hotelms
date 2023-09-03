from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, DateTimeField, FloatField

from core.models import Service, TypeService
from hebergement.models import Reservation, Chambre


class Restaurant(Service):
    designation = CharField(max_length=25, verbose_name="désignation")

    def __str__(self):
        return f'Restaurant {self.designation}' if self is not None else ''

    def save(self, *args, **kwargs):
        self.type = TypeService.objects.filter(designation__iexact='restauration').first()
        super().save(*args, **kwargs)


class ReservationRestaurant(models.Model):
    reservation = ForeignKey(Reservation, on_delete=CASCADE, verbose_name='réservation')
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE, verbose_name='restaurant')
    montant = FloatField(default=0)


    def __str__(self):
        return f'Le client de #{self.reservation}# a mangé à/au  {self.restaurant}' if self is not None else ''
