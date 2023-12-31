# Generated by Django 4.2.4 on 2023-08-31 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hebergement', '0003_alter_reservation_date_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='pickup',
            field=models.BooleanField(default=False, verbose_name='nécessite un transfert (pickup)?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_commande',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 19, 43, 37, 522229, tzinfo=datetime.timezone.utc), verbose_name='date de la commande'),
        ),
    ]
