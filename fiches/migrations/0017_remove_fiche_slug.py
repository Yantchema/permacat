# Generated by Django 2.1.11 on 2019-11-08 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0016_auto_20191108_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiche',
            name='slug',
        ),
    ]
