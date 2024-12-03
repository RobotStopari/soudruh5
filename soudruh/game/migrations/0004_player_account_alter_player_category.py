# Generated by Django 5.1.3 on 2024-12-03 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_player_category_alter_room_game_starting_money'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('BEZ', 'Bezpartijní'), ('GEN', 'Generální Tajemník ÚV Strany'), ('UV', 'Člen Ústředního Výboru'), ('POS', 'Poslanec'), ('KAN', 'Kandidát'), ('POL', 'Člen Politbyra ÚV'), ('KOM', 'Člen Strany')], default='Bezpartijní', max_length=200, null=True),
        ),
    ]