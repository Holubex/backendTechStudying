# Generated by Django 4.1.1 on 2024-06-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_actor_alter_country_options_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='death_date',
            field=models.DateField(blank=True),
        ),
    ]