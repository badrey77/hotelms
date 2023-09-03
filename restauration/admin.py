from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restauration.models import Restaurant, ReservationRestaurant


@admin.register(Restaurant)
class RestaurantConfig(ModelAdmin):
    list_display = ["designation"]
    search_fields = ["designation"]


@admin.register(ReservationRestaurant)
class ReservationRestaurantConfig(ModelAdmin):
    autocomplete_fields = ["restaurant", "reservation"]
    list_filter = ["restaurant"]
    search_fields = ["reservation__num", "reservation__demandeur__nom", "reservation__demandeur__prenom"]
