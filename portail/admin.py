from django.apps.registry import Apps
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import DefaultAdminSite
from django.contrib.auth.admin import admin
from hebergement.models import Reservation
from hebergement.admin import ReservationConfig
from portail.models import Dummy


class ModelNewMeta:
    proxy = True
    app_label = Dummy._meta.app_label


# reservation_model = type("Reservation", (Reservation,), {'__module__': '', 'Meta': ModelNewMeta})
# admin.site.register(reservation_model)
