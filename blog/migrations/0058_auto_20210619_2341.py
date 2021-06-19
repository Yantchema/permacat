# Generated by Django 2.2.24 on 2021-06-19 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0057_auto_20210619_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Album', verbose_name='Album photo associé'),
        ),
    ]
