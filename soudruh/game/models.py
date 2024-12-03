from django.db import models
from django.contrib.auth.models import User

from colorfield.fields import ColorField
from django.conf import settings

CATEGORIES = {
        ('1-BEZ', 'Bezpartijní'),
        ('2-KAN', 'Kandidát'),
        ('3-KOM', 'Člen Strany'),
        ('4-POS', 'Poslanec'),
        ('5-UV', 'Člen Ústředního Výboru'),
        ('6-POL', 'Člen Politbyra ÚV'),
        ('7-GEN', 'Generální Tajemník ÚV Strany'),
        }



class Room(models.Model):
    room_name = models.CharField(max_length=200, null=True)
    
    game_starting_money = models.IntegerField(null=True, blank=True, default=2000)
    
    def __str__(self):
        return self.room_name
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'



class Player(models.Model):
    
    account = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    
    #player
    color = ColorField(default='#FF0000', null=True)
    
    #game data
    pindex = models.IntegerField(null=True, default=0)
    money = models.IntegerField(null=True, default=0)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES, default='1-BEZ')
    marcs = models.IntegerField(null=True, default=0)
    
    #equipment
    looks_like_stalin = models.BooleanField(default=False)
    propustka = models.BooleanField(default=False)
    proverka = models.BooleanField(default=False)
    nuzky = models.BooleanField(default=False)
    vesta = models.BooleanField(default=False)
    plan_zaminovani = models.BooleanField(default=False)
    
    #game status
    active = models.BooleanField(default=False)
    on_move = models.BooleanField(default=False)
    skipped = models.IntegerField(null=True, default=0)
    wait_moves = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.account.username
    
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    
class Postih(models.Model):
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    message = models.CharField(max_length=2000, null=True, blank=True)
    code = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Postih'
        verbose_name_plural = 'Postihy'
    
class Vylepseni(models.Model):
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    message = models.CharField(max_length=2000, null=True, blank=True)
    code = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Vylepšení'
        verbose_name_plural = 'Vylepšení'
        
class Message(models.Model):
    header = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=2000, null=True, blank=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'