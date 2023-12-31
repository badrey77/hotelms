# Generated by Django 4.2.4 on 2023-08-31 14:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentIdentification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=1000, verbose_name='n° du document')),
                ('type_document', models.CharField(choices=[('CN', 'Carte ID Nationale'), ('PS', 'Passport'), ('PC', 'Permi de Conduire')], max_length=2, verbose_name='type du document')),
                ('num_id', models.CharField(default='ND', max_length=100, verbose_name='n° ID national')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=1000, verbose_name='désignation')),
                ('abbr', models.CharField(max_length=5, verbose_name='abbréviation')),
                ('contact', models.CharField(max_length=1000, verbose_name='informations de contact')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1000, verbose_name='nom')),
                ('abbr', models.CharField(max_length=5, verbose_name='abbréviation')),
                ('code', models.CharField(max_length=5, verbose_name='code téléphone')),
                ('date_delivrance', models.DateField(verbose_name='date de délivrance')),
                ('valide_jusqua', models.DateField(verbose_name="valide jusqu'à")),
                ('autorite', models.CharField(max_length=1000, verbose_name='autorité de délivrance')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=1000, verbose_name='nom')),
                ('prenom', models.CharField(max_length=1000, verbose_name='prénom')),
                ('sexe', models.CharField(choices=[('M', 'MASCULIN'), ('F', 'FEMININ')], default='M', max_length=1)),
                ('date_naissance', models.DateField(default=datetime.date(2021, 8, 31), verbose_name='date de naissance')),
                ('document_identification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.documentidentification')),
                ('pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citoyens', to='core.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.personne')),
                ('appartenance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membres', to='core.organisation')),
            ],
            bases=('core.personne',),
        ),
    ]
