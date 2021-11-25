# Generated by Django 2.2.24 on 2021-11-24 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20210917_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposition', models.CharField(max_length=500, verbose_name='Proposition')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Question_majoritaire')),
            ],
        ),
    ]
