# Generated by Django 5.1.3 on 2024-12-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_remove_player_name_alter_player_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('2-KAN', 'Kandidát'), ('1-BEZ', 'Bezpartijní'), ('6-POL', 'Člen Politbyra ÚV'), ('5-UV', 'Člen Ústředního Výboru'), ('3-KOM', 'Člen Strany')], default='1-BEZ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postih',
            name='category',
            field=models.CharField(choices=[('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('2-KAN', 'Kandidát'), ('1-BEZ', 'Bezpartijní'), ('6-POL', 'Člen Politbyra ÚV'), ('5-UV', 'Člen Ústředního Výboru'), ('3-KOM', 'Člen Strany')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vylepseni',
            name='category',
            field=models.CharField(choices=[('4-POS', 'Poslanec'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('2-KAN', 'Kandidát'), ('1-BEZ', 'Bezpartijní'), ('6-POL', 'Člen Politbyra ÚV'), ('5-UV', 'Člen Ústředního Výboru'), ('3-KOM', 'Člen Strany')], max_length=200, null=True),
        ),
    ]
