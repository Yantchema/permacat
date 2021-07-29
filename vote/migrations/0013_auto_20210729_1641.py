# Generated by Django 2.2.24 on 2021-07-29 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0012_auto_20210729_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='choix',
        ),
        migrations.CreateModel(
            name='ReponseQuestion_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(choices=[('', '-----------'), ('0', "pas du tout d'accord"), ('1', "Plutot pas d'accord"), ('2', 'Neutre'), ('3', "Plutot d'accord"), ('4', "Tout à fait d'accord")], default='', max_length=30, verbose_name='Choix du vote :')),
                ('question_b', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vote.Question_majoritaire')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rep_question_m', to='vote.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='ReponseQuestion_b',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(choices=[('', '-----------'), ('0', 'Oui'), ('1', 'Non'), ('2', 'Ne se prononce pas')], default='', max_length=30, verbose_name='Choix du vote :')),
                ('question_b', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vote.Question_binaire')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rep_question_b', to='vote.Vote')),
            ],
        ),
    ]
