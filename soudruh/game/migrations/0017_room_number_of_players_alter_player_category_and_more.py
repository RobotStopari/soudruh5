# Generated by Django 4.2.17 on 2025-01-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_player_is_room_admin_alter_player_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='number_of_players',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('6-POL', 'Člen Politbyra ÚV'), ('7-GEN', 'Generální Tajemník ÚV Strany')], default='1-BEZ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postih',
            name='category',
            field=models.CharField(choices=[('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('6-POL', 'Člen Politbyra ÚV'), ('7-GEN', 'Generální Tajemník ÚV Strany')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='actual_player',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vylepseni',
            name='category',
            field=models.CharField(choices=[('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('6-POL', 'Člen Politbyra ÚV'), ('7-GEN', 'Generální Tajemník ÚV Strany')], max_length=200, null=True),
        ),
    ]