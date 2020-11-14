# Generated by Django 2.2.13 on 2020-08-17 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_auto_20200615_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suffrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_vote', models.CharField(choices=[('', '-----------'), ('0', "Vote d'un projet"), ('1', "Vote d'une décision"), ('2', 'Sondage')], default='', max_length=30, verbose_name='Type de vote')),
                ('question', models.CharField(max_length=100, verbose_name='Question soumise au vote ?')),
                ('slug', models.SlugField(max_length=100)),
                ('contenu', models.TextField(null=True, verbose_name='Description')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('estPublic', models.BooleanField(default=False, verbose_name='Public ou réservé aux membres permacat')),
                ('date_dernierMessage', models.DateTimeField(auto_now=True, verbose_name='Date du dernier message')),
                ('date_modification', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification')),
                ('estArchive', models.BooleanField(default=False, verbose_name='Archiver la proposition')),
                ('estAnonyme', models.BooleanField(default=False, verbose_name='Vote anonyme')),
                ('start_time', models.DateTimeField(help_text='jj/mm/année', null=True, verbose_name='Date de début')),
                ('end_time', models.DateTimeField(help_text='jj/mm/année', null=True, verbose_name='Date de fin')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur_suffrage', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'suffrage',
                'ordering': ('-date_creation',),
            },
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='votation',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='votation',
        ),
        migrations.DeleteModel(
            name='Votation',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='suffrage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Suffrage'),
        ),
        migrations.AddField(
            model_name='vote',
            name='suffrage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suffrage', to='vote.Suffrage'),
        ),
    ]