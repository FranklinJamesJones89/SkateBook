# Generated by Django 4.1.7 on 2023-03-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0004_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='spot',
            name='state',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='street',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='zipcode',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]