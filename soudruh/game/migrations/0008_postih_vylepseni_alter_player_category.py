# Generated by Django 5.1.3 on 2024-12-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_remove_room_actual_player_player_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postih',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV')], max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=2000, null=True)),
                ('code', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vylepseni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV')], max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=2000, null=True)),
                ('code', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('4-POS', 'Poslanec'), ('3-KOM', 'Člen Strany'), ('7-GEN', 'Generální Tajemník ÚV Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('1-BEZ', 'Bezpartijní'), ('2-KAN', 'Kandidát'), ('6-POL', 'Člen Politbyra ÚV')], default='1-BEZ', max_length=200, null=True),
        ),
    ]
