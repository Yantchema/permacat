# Generated by Django 2.2.13 on 2021-03-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_suffrage_asso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='commentaire',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire'),
        ),
    ]