# Generated by Django 4.2.4 on 2023-09-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_personne_date_naissance'),
        ('hebergement', '0014_alter_reservation_date_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='services_inclus',
            field=models.ManyToManyField(blank=True, to='core.typeservice', verbose_name='services inclus'),
        ),
    ]