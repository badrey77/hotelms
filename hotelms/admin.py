from django.contrib.admin import AdminSite
from core.forms import CalendarForm, WelcomeFormSet


class MyAdminSite(AdminSite):
    AdminSite.site_header = 'SYSTEME DE GESTION D\'HOTEL'
    AdminSite.site_title = 'SGH'
    AdminSite.index_title = 'ACCUEIL'
    AdminSite.index_template = 'admin/index.html'
    # def index(self, request, extra_context=None):
    # extra_context = {'form': CalendarForm()}
    #     super().index(request=request, extra_context=extra_context)

    def index(self, request, extra_context=None):
        extra_context = {'form': WelcomeFormSet()}
        return super().index(request,extra_context)


