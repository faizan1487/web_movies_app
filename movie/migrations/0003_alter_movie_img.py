# Generated by Django 5.0.6 on 2024-05-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]