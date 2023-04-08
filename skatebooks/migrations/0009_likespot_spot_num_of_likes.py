# Generated by Django 4.1.7 on 2023-04-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatebooks', '0008_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_id', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='spot',
            name='num_of_likes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]