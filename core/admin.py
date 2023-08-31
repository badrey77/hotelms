from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin, TabularInline

from core.models import Organisation, Client, Pays, DocumentIdentification, Personne, Classe, ServiceClasse, Service
from hebergement.models import Agent

# Configure AdminSite ...
AdminSite.site_header = 'SYSTEME DE GESTION D\'HOTEL'
AdminSite.site_title = 'SGH'
AdminSite.index_title = 'ACCUEIL'


# Administration de l'appli : Core App ...
@admin.register(Personne)
class PersonneConfig(ModelAdmin):
    list_display = ['nom', 'prenom']


@admin.register(Client)
class ClientConfig(ModelAdmin):
    list_display = ['nom', 'prenom']


@admin.register(Agent)
class AgentConfig(ModelAdmin):
    list_display = ['nom', 'prenom']


@admin.register(Pays)
class PaysConfig(ModelAdmin):
    list_display = ['nom', 'abbr', 'code']


@admin.register(DocumentIdentification)
class DocumentIdentificationConfig(ModelAdmin):
    list_display = ['num_doc', 'type_document', 'personne', 'valide_jusqua']


class MembreInline(TabularInline):
    model = Client
    extra = 0


@admin.register(Organisation)
class OrganisationConfig(ModelAdmin):
    list_display = ['designation', 'contact']
    inlines = [MembreInline]


@admin.register(Classe)
class ClasseConfig(ModelAdmin):
    list_display = ['designation']


@admin.register(Service)
class ServiceConfig(ModelAdmin):
    list_display = ['type']


@admin.register(ServiceClasse)
class ServiceClasseConfig(ModelAdmin):
    list_display = ['classe', 'service', 'prix']