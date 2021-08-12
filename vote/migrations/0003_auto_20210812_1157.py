# Generated by Django 2.2.24 on 2021-08-12 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20210805_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_binaire',
            name='question',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Question (oui/non) soumise au vote ?'),
        ),
        migrations.AlterField(
            model_name='question_majoritaire',
            name='question',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Question (jugement majoritaire) soumise au vote :'),
        ),
        migrations.AlterField(
            model_name='reponsequestion_b',
            name='choix',
            field=models.IntegerField(choices=[('', '-----------'), (0, 'Oui'), (1, 'Non'), (2, 'Ne se prononce pas')], default='', verbose_name='Choix du vote :'),
        ),
        migrations.AlterField(
            model_name='reponsequestion_m',
            name='choix',
            field=models.IntegerField(choices=[('', '-----------'), (0, "pas du tout d'accord"), (1, "Plutot pas d'accord"), (2, 'Neutre'), (3, "Plutot d'accord"), (4, "Tout à fait d'accord")], default='', verbose_name='Choix du vote :'),
        ),
    ]
