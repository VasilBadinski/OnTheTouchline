# Generated by Django 5.2.3 on 2025-07-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_player_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leagues',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
