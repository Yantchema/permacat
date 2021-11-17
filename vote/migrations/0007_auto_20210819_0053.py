# Generated by Django 2.2.24 on 2021-08-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_auto_20210819_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suffrage',
            name='type_vote',
            field=models.CharField(choices=[('', '-----------'), ('0', "Vote d'un projet"), ('1', "Vote d'une décision"), ('2', 'Sondage'), ('3', 'Election')], default='', max_length=30, verbose_name='Type de vote'),
        ),
    ]