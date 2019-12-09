# Generated by Django 2.2.8 on 2019-12-09 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ateliers', '0010_remove_atelier_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date_atelier',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date prévue'),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='heure_atelier',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, help_text='Heure prévue', null=True, verbose_name='Heure prévue'),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='titre',
            field=models.CharField(max_length=120, verbose_name="Titre de l'atelier"),
        ),
    ]
