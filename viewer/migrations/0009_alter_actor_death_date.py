# Generated by Django 4.1.1 on 2024-06-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_alter_actor_death_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
