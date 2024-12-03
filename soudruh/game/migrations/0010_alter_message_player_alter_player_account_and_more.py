# Generated by Django 5.1.3 on 2024-12-03 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_alter_player_options_alter_postih_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('1-BEZ', 'Bezpartijní'), ('5-UV', 'Člen Ústředního Výboru'), ('2-KAN', 'Kandidát')], default='1-BEZ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postih',
            name='category',
            field=models.CharField(choices=[('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('1-BEZ', 'Bezpartijní'), ('5-UV', 'Člen Ústředního Výboru'), ('2-KAN', 'Kandidát')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vylepseni',
            name='category',
            field=models.CharField(choices=[('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('1-BEZ', 'Bezpartijní'), ('5-UV', 'Člen Ústředního Výboru'), ('2-KAN', 'Kandidát')], max_length=200, null=True),
        ),
    ]