from django.apps.registry import Apps
from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin, TabularInline
from django.contrib.admin.sites import DefaultAdminSite

from core.forms import CalendarForm
from core.models import Organisation, Client, Pays, DocumentIdentification, Personne, Classe, ServiceClasse, Service, \
    TypeService
from hebergement.models import Agent


@admin.register(Personne)
class PersonneConfig(ModelAdmin):
    list_display = ['nom', 'prenom']
    search_fields = ['nom', 'prenom']


@admin.register(Client)
class ClientConfig(ModelAdmin):
    list_display = ['nom', 'prenom']
    search_fields = ['nom', 'prenom']


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


@admin.register(TypeService)
class TypeServiceConfig(ModelAdmin):
    list_display = ['designation']


# @admin.register(Service)
# class ServiceConfig(ModelAdmin):
#     list_display = ['type']


# @admin.register(ServiceClasse)
# class ServiceClasseConfig(ModelAdmin):
#     list_display = ['classe', 'service', 'prix']


class ServiceClasseInline(TabularInline):
    model = ServiceClasse
    verbose_name = 'tarification du service'
    verbose_name_plural = 'tarifications de services'


@admin.register(Classe)
class ClasseConfig(ModelAdmin):
    list_display = ['designation']
    inlines = [ServiceClasseInline]