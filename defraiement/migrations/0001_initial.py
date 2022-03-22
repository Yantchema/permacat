# Generated by Django 2.2.24 on 2022-02-04 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0080_auto_20211203_1927'),
        ('bourseLibre', '0064_auto_20220205_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('1', 'Troc de Graine'), ('0', 'Rencontre'), ('2', 'Atelier'), ('3', 'Autre')], default='0', max_length=30, verbose_name='categorie')),
                ('titre', models.CharField(max_length=120, verbose_name='Titre de la rencontre')),
                ('slug', models.SlugField(default=uuid.uuid4, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_time', models.DateField(blank=True, default=django.utils.timezone.now, help_text='(jj/mm/an)', null=True, verbose_name='Date de la rencontre')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('date_modification', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification')),
                ('estArchive', models.BooleanField(default=False, verbose_name='Archiver la réunion')),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bourseLibre.Adresse')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('asso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bourseLibre.Asso')),
                ('auteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_creation',),
            },
        ),
        migrations.CreateModel(
            name='ParticipantReunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, verbose_name='Nom du participant')),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bourseLibre.Adresse')),
                ('reunion', models.ManyToManyField(help_text="Le participant doit etre associé à une reunion existante (sinon créez d'abord la reunion)", to='defraiement.Reunion')),
            ],
        ),
    ]