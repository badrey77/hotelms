# Generated by Django 4.2.4 on 2023-08-31 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hebergement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_commande',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 19, 3, 39, 361382, tzinfo=datetime.timezone.utc), verbose_name='date de la commande'),
        ),
    ]