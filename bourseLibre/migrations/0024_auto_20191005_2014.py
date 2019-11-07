# Generated by Django 2.1.11 on 2019-10-05 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0023_auto_20191002_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]