# Generated by Django 2.2.13 on 2020-10-30 19:06

from django.db import migrations
from bourseLibre.settings.production import SERVER_EMAIL

def create_types(apps, schema_editor):
    assos = apps.get_model('bourseLibre', 'Asso')
    #asso_jp , created = assos.objects.get_or_create(nom='Jardins Partagés', abreviation="jp", email=SERVER_EMAIL)

class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0037_auto_20201030_1913'),
    ]

    operations = [
        migrations.RunPython(create_types),
    ]
