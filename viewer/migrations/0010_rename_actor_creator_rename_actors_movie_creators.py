# Generated by Django 4.1.1 on 2024-06-02 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_alter_actor_death_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actor',
            new_name='Creator',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='actors',
            new_name='creators',
        ),
    ]
