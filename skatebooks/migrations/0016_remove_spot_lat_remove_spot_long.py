# Generated by Django 4.1.7 on 2023-04-26 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0015_spot_lat_spot_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='long',
        ),
    ]
