# Generated by Django 4.1.1 on 2024-06-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_alter_genre_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='movies', to='viewer.genre'),
        ),
    ]
