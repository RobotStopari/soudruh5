# Generated by Django 4.2.17 on 2025-01-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0032_history_type_alter_notification_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sad', 'Postih'), ('happy', 'Vylepšení')], max_length=200, null=True)),
                ('category', models.CharField(choices=[('7-GEN', 'Generální Tajemník ÚV Strany'), ('2-KAN', 'Kandidát'), ('4-POS', 'Poslanec'), ('1-BEZ', 'Bezpartijní'), ('3-KOM', 'Člen Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('6-POL', 'Člen Politbyra ÚV')], max_length=200, null=True)),
                ('notification_message', models.CharField(blank=True, max_length=2000, null=True)),
                ('history_record_message_p1', models.CharField(blank=True, max_length=2000, null=True)),
                ('history_record_message_p2', models.CharField(blank=True, max_length=2000, null=True)),
                ('pindex_change_by', models.IntegerField(default=0, null=True)),
                ('pindex_set_to', models.IntegerField(default=0, null=True)),
                ('money_change_by', models.IntegerField(default=0, null=True)),
                ('wait_moves_set_to', models.IntegerField(default=0, null=True)),
                ('give_stalin', models.BooleanField(default=False)),
                ('give_propustka', models.BooleanField(default=False)),
                ('give_proverka', models.BooleanField(default=False)),
                ('give_nuzky', models.BooleanField(default=False)),
                ('give_vesta', models.BooleanField(default=False)),
                ('give_plan_zaminovani', models.BooleanField(default=False)),
                ('give_everybody', models.IntegerField(default=0, null=True)),
                ('remove_from_everybody', models.IntegerField(default=0, null=True)),
                ('money_change_by_per_player', models.IntegerField(default=0, null=True)),
                ('go_to_vezeni', models.BooleanField(default=False)),
                ('go_to_blazinec', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Efekt',
                'verbose_name_plural': 'Efekty',
            },
        ),
        migrations.DeleteModel(
            name='Postih',
        ),
        migrations.DeleteModel(
            name='Vylepseni',
        ),
        migrations.AlterField(
            model_name='player',
            name='category',
            field=models.CharField(choices=[('7-GEN', 'Generální Tajemník ÚV Strany'), ('2-KAN', 'Kandidát'), ('4-POS', 'Poslanec'), ('1-BEZ', 'Bezpartijní'), ('3-KOM', 'Člen Strany'), ('5-UV', 'Člen Ústředního Výboru'), ('6-POL', 'Člen Politbyra ÚV')], default='1-BEZ', max_length=200, null=True),
        ),
    ]
