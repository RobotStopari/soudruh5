# Generated by Django 4.2.17 on 2025-01-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_room_number_of_players_alter_player_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postih',
            name='code',
        ),
        migrations.RemoveField(
            model_name='vylepseni',
            name='code',
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('1-BEZ', 'Bezpartijní'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru')], default='1-BEZ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postih',
            name='category',
            field=models.CharField(choices=[('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('1-BEZ', 'Bezpartijní'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vylepseni',
            name='category',
            field=models.CharField(choices=[('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV'), ('3-KOM', 'Člen Strany'), ('1-BEZ', 'Bezpartijní'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru')], max_length=200, null=True),
        ),
    ]
