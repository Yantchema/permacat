# Generated by Django 2.1.7 on 2019-03-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190305_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(choices=[('Annonce', 'Annonce'), ('Agenda', 'Agenda'), ('Jardinage', 'Jardinage'), ('Recette', 'Recette'), ('Histoire', 'Histoire'), ('Bricolage', 'Bricolage'), ('Culture', 'Culture'), ('Bon_plan', 'Bon plan'), ('Point', 'Point de vue'), ('Annonce', 'Annonce'), ('Autre', 'Autre')], default='Annonce', max_length=30, verbose_name='categorie'),
        ),
    ]