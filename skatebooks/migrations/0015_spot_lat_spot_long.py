# Generated by Django 4.1.7 on 2023-04-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0014_remove_spot_lat_remove_spot_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='lat',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
