# Generated by Django 4.2.4 on 2023-08-31 14:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pays',
            name='autorite',
        ),
        migrations.RemoveField(
            model_name='pays',
            name='date_delivrance',
        ),
        migrations.RemoveField(
            model_name='pays',
            name='valide_jusqua',
        ),
        migrations.AddField(
            model_name='documentidentification',
            name='autorite',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000, verbose_name='autorité de délivrance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentidentification',
            name='date_delivrance',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date de délivrance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentidentification',
            name='valide_jusqua',
            field=models.DateField(default=django.utils.timezone.now, verbose_name="valide jusqu'à"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personne',
            name='date_naissance',
            field=models.DateField(default=datetime.date(2005, 8, 31), verbose_name='date de naissance'),
        ),
    ]
