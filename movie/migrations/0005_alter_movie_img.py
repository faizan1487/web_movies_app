# Generated by Django 5.0.6 on 2024-05-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_remove_movie_imgpath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
