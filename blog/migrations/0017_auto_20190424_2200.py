# Generated by Django 2.1.3 on 2019-04-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_article_estmodifiable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(choices=[('Annonce', 'Annonce'), ('Agenda', 'Agenda'), ('Rencontre', 'Rencontre'), ('Entraide', 'Entraide'), ('Chantier', 'Chantier participatif'), ('Jardinage', 'Jardinage'), ('Recette', 'Recette'), ('Bricolage', 'Bricolage'), ('Culture', 'Culture'), ('Bon_plan', 'Bon plan'), ('Point', 'Point de vue'), ('Autre', 'Autre')], default='Annonce', max_length=30, verbose_name='categorie'),
        ),
    ]
