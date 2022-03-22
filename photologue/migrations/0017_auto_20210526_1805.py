# Generated by Django 2.2.20 on 2021-05-26 16:05

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0016_auto_20210526_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'get_latest_by': 'date_added', 'ordering': ['-date_added'], 'verbose_name': 'album', 'verbose_name_plural': 'albums'},
        ),
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='albums', to='photologue.Photo', verbose_name='photos'),
        ),
    ]