# Generated by Django 4.1.7 on 2023-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0012_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spot',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
