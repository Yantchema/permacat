# Generated by Django 2.2.8 on 2019-12-09 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ateliers', '0008_auto_20191209_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='atelier',
            name='heure_atelier',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Heure prévue'),
        ),
    ]
