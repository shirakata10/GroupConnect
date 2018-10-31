# Generated by Django 2.0.5 on 2018-10-31 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupConnect', '0002_auto_20181017_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='rome_name',
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, db_column='first_name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, db_column='last_name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='rome_first_name',
            field=models.CharField(blank=True, db_column='rome_first_name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='rome_last_name',
            field=models.CharField(blank=True, db_column='rome_last_name', max_length=100, null=True),
        ),
    ]
