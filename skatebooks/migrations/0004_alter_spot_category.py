# Generated by Django 4.1.7 on 2023-03-31 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0003_category_remove_user_bio_user_hometown_spot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='skatebooks.category'),
        ),
    ]
