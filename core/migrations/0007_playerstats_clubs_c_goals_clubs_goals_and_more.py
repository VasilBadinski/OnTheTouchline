# Generated by Django 5.2.3 on 2025-07-23 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_clubs_league_alter_clubs_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='players', serialize=False, to='core.player')),
                ('played_games', models.PositiveIntegerField(default=0)),
                ('goals', models.PositiveIntegerField(default=0)),
                ('assists', models.PositiveIntegerField(default=0)),
                ('yellow_cards', models.PositiveIntegerField(default=0)),
                ('red_cards', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='clubs',
            name='c_goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clubs',
            name='goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clubs',
            name='played_games',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clubs',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clubs',
            name='s_goals',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
