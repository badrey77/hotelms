# Generated by Django 4.2.4 on 2023-09-01 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_classe_service_serviceclasse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='date_naissance',
            field=models.DateField(default=datetime.date(2005, 9, 1), verbose_name='date de naissance'),
        ),
    ]
