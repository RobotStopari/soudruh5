# Generated by Django 4.2.17 on 2025-01-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0038_alter_effect_category_alter_player_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effect',
            name='category',
            field=models.CharField(choices=[('5-UV', 'Člen Ústředního Výboru'), ('2-KAN', 'Kandidát'), ('1-BEZ', 'Bezpartijní'), ('3-KOM', 'Člen Strany'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('6-POL', 'Člen Politbyra ÚV')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('5-UV', 'Člen Ústředního Výboru'), ('2-KAN', 'Kandidát'), ('1-BEZ', 'Bezpartijní'), ('3-KOM', 'Člen Strany'), ('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('6-POL', 'Člen Politbyra ÚV')], default='1-BEZ', max_length=200, null=True),
        ),
    ]
