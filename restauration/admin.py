from django.contrib import admin
from django.contrib.admin import ModelAdmin

from restauration.models import Restaurant, ReservationRestaurant


@admin.register(Restaurant)
class RestaurantConfig(ModelAdmin):
    list_filter = ["designation"]


@admin.register(ReservationRestaurant)
class ReservationRestaurantConfig(ModelAdmin):
    raw_id_fields = ["restaurant", "reservation"]
