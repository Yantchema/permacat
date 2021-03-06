# Generated by Django 2.1.11 on 2019-11-04 15:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0002_auto_20191104_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('0', 'Observation'), ('1', 'Experience'), ('2', 'Jardinage')], default='0', max_length=30, verbose_name='categorie')),
                ('titre', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('contenu', models.TextField(null=True)),
                ('age', models.CharField(choices=[('0', 'facile'), ('1', 'moyen'), ('2', 'difficile')], default='0', max_length=30, verbose_name='age')),
                ('difficulte', models.CharField(choices=[('0', '3-6 ans'), ('1', '7-11 ans'), ('2', '12 ans et plus')], default='0', max_length=30, verbose_name='difficultÃ©')),
                ('budget', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=30, verbose_name='budget')),
                ('temps', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=30, verbose_name='temps')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('date_modification', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de modification')),
            ],
            options={
                'ordering': ('-date_creation',),
            },
        ),
        migrations.RemoveField(
            model_name='fiche',
            name='estPublic',
        ),
        migrations.AddField(
            model_name='fiche',
            name='en_savoir_plus',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fiche',
            name='statut',
            field=models.CharField(choices=[('0', 'proposition'), ('1', "en cours d'Ã©criture"), ('2', 'achevÃ©e mais pas validÃ©e'), ('3', 'validÃ©e')], default='proposition', max_length=30, verbose_name='statut de la fiche'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='categorie',
            field=models.CharField(choices=[('0', 'Bases de la permaculture'), ('1', 'conception'), ('2', 'RÃ©alisation'), ('3', 'RÃ©colte')], default='0', max_length=30, verbose_name='categorie'),
        ),
        migrations.AddField(
            model_name='atelier',
            name='fiche',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiches.Fiche'),
        ),
    ]
