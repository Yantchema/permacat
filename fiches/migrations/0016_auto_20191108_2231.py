# Generated by Django 2.1.11 on 2019-11-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0015_auto_20191108_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='titre',
            field=models.CharField(max_length=120),
        ),
    ]
