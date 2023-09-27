# Generated by Django 4.2.4 on 2023-09-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_personne_date_naissance'),
        ('hebergement', '0019_rename_personne_reservation_personnes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationchambre',
            name='personnes',
            field=models.ManyToManyField(blank=True, null=True, to='core.client'),
        ),
    ]
