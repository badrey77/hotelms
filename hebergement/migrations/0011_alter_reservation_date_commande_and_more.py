# Generated by Django 4.2.4 on 2023-09-01 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_typeservice_alter_service_type_and_more'),
        ('hebergement', '0010_alter_reservation_date_commande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_commande',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 17, 2, 49, 755508, tzinfo=datetime.timezone.utc), verbose_name='date de la commande'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='services_inclus',
            field=models.ManyToManyField(blank=True, null=True, to='core.typeservice', verbose_name='services inclus'),
        ),
    ]
