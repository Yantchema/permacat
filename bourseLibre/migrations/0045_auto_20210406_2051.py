# Generated by Django 2.2.13 on 2021-04-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0044_remove_profil_cotisation_a_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='date_dernierMessage',
            field=models.DateTimeField(verbose_name='Date de Modification'),
        ),
    ]