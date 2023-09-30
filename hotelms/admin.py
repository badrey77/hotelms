from django.contrib.admin import AdminSite
from core.forms import WelcomeForm
from core.models import Client
from hebergement.models import Chambre


class MyAdminSite(AdminSite):
    AdminSite.site_header = 'SYSTEME DE GESTION D\'HOTEL'
    AdminSite.site_title = 'SGH'
    AdminSite.index_title = 'ACCUEIL'
    AdminSite.index_template = 'admin/index.html'
    # def index(self, request, extra_context=None):
    # extra_context = {'form': CalendarForm()}
    #     super().index(request=request, extra_context=extra_context)

    def index(self, request, extra_context=None):

        extra_context = {
            'chambres_libres': WelcomeForm(Chambre.nbr_chambres_libres(),'dessin2.png'),
            'clients_residents': WelcomeForm(Client.objects.all().count(),'dessin5.png'),
            'taux_occupation': WelcomeForm(Chambre.taux_occupation(),'dessin9.png')
        }
        return super().index(request,extra_context)


