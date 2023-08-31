import datetime

from django.db import models
from django.db.models import CharField, DateField, ForeignKey, CASCADE, OneToOneField

SEXE = (
    ('M', 'MASCULIN'),
    ('F', 'FEMININ'),
)

TYPE_DOCUMENT_IDENTITE = (
    ('CN', 'Carte ID Nationale'),
    ('PS', 'Passport'),
    ('PC', 'Permis de Conduire'),
)


class DocumentIdentification(models.Model):
    num_doc = CharField(max_length=1000, verbose_name='n° du document')
    type_document = CharField(max_length=2, choices=TYPE_DOCUMENT_IDENTITE, verbose_name='type du document')
    num_id = CharField(max_length=100, verbose_name='n° ID national', default='ND')
    date_delivrance = DateField(verbose_name='date de délivrance')
    valide_jusqua = DateField(verbose_name='valide jusqu\'à')
    autorite = CharField(max_length=1000, verbose_name='autorité de délivrance')

    def __str__(self):
        if self:
            return f'{self.nom} ({self.abbr}, {self.code})'
        return ''

    class Meta:
        verbose_name_plural = "documents d'identification"


class Pays(models.Model):
    nom = CharField(max_length=1000, verbose_name='nom')
    abbr = CharField(max_length=5, verbose_name='abbréviation')
    code = CharField(max_length=5, verbose_name='code téléphone')

    def __str__(self):
        if self:
            return f'{self.nom} ({self.abbr}, {self.code})'
        return ''

    class Meta:
        verbose_name_plural = 'pays'


class Personne(models.Model):
    nom = CharField(max_length=1000, verbose_name='nom')
    prenom = CharField(max_length=1000, verbose_name='prénom')
    sexe = CharField(max_length=1, choices=SEXE, default='M')
    date_naissance = DateField(default=datetime.date.today()-datetime.timedelta(6574), verbose_name='date de naissance')
    pays = ForeignKey(Pays, on_delete=CASCADE, related_name='citoyens')
    document_identification = OneToOneField(DocumentIdentification, on_delete=CASCADE)

    def age(self):
        years = 0
        if self:
            fl_years = (datetime.date.today() - self.date_naissance).days / 365.25
            years = int(fl_years)
        return years

    def __str__(self):
        if self:
            return f'{self.nom} {self.prenom} ({self.age()} - {self.sexe})'
        return ''


class Organisation(models.Model):
    designation = CharField(max_length=1000, verbose_name='désignation')
    abbr = CharField(max_length=5, verbose_name='abbréviation')
    contact = CharField(max_length=1000, verbose_name='informations de contact')

    def __str__(self):
        return self.designation if (self is not None) else ''


class Client(Personne):
    appartenance = ForeignKey(Organisation, on_delete=CASCADE, related_name='membres', null=True, blank=True)

    def __str__(self):
        return super().__str__()
