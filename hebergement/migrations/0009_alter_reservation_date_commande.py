# Generated by Django 4.2.4 on 2023-09-01 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hebergement', '0008_remove_salle_id_salle_service_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_commande',
            field=models.DateField(default=datetime.datetime(2023, 9, 1, 12, 46, 17, 17371, tzinfo=datetime.timezone.utc), verbose_name='date de la commande'),
        ),
    ]