# Generated by Django 2.2.8 on 2020-06-08 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('Discu', 'Discussion générale'), ('Coordination', 'Coordination'), ('Potager', 'Potager'), ('PPAM', 'PPAM'), ('Arbres', 'Arbres'), ('Administratif', 'Administratif'), ('Agenda', 'Agenda'), ('Documentation', 'Documentation'), ('Autre', 'Autre')], default='Annonce', max_length=30, verbose_name='categorie')),
                ('titre', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('date_modification', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification')),
                ('estPublic', models.BooleanField(default=False, verbose_name='Public ou réservé aux membres permacat')),
                ('estModifiable', models.BooleanField(default=False, verbose_name="Modifiable par n'importe qui")),
                ('date_dernierMessage', models.DateTimeField(auto_now=True, verbose_name='Date du dernier message')),
                ('dernierMessage', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('estArchive', models.BooleanField(default=False, verbose_name="Archiver l'article")),
                ('start_time', models.DateTimeField(blank=True, help_text='jj/mm/année', null=True, verbose_name="Date de début (optionnel, affichage dans l'agenda)")),
                ('end_time', models.DateTimeField(blank=True, help_text='jj/mm/année', null=True, verbose_name="Date de fin (optionnel, pour affichage dans l'agenda)")),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur_article_jardin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article_jardin',
                'ordering': ('-date_creation',),
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_jardin', to='jardinpartage.Article')),
                ('auteur_comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur_comm_jardin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'commentaire_jardin',
            },
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name="Titre de l'événement (si laissé vide, ce sera le titre de l'article)")),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, help_text='jj/mm/année', verbose_name='Date')),
                ('end_time', models.DateTimeField(blank=True, help_text='jj/mm/année', null=True, verbose_name='Date de fin (optionnel pour un evenement sur plusieurs jours)')),
                ('article', models.ForeignKey(help_text="L'evenement doit etre associé à un article existant (sinon créez un article avec une date)", on_delete=django.db.models.deletion.CASCADE, to='jardinpartage.Article')),
            ],
            options={
                'db_table': 'evenement_jardin',
                'unique_together': {('article', 'start_time')},
            },
        ),
    ]