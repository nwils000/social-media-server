# Generated by Django 5.0.6 on 2024-06-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social_media', '0005_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='/media/images/Alien_upNV4mo.png', upload_to='images/'),
            preserve_default=False,
        ),
    ]
