from django.db import models
from django.contrib.auth.models import User

from colorfield.fields import ColorField

from djsingleton.models import SingletonModel, SingletonActiveModel

class Config(SingletonModel):
    cube_size = models.IntegerField(default=6)

CATEGORIES = {
        ('1-BEZ', 'Bezpartijní'),
        ('2-KAN', 'Kandidát'),
        ('3-KOM', 'Člen Strany'),
        ('4-POS', 'Poslanec'),
        ('5-UV', 'Člen Ústředního Výboru'),
        ('6-POL', 'Člen Politbyra ÚV'),
        ('7-GEN', 'Generální Tajemník ÚV Strany'),
        }

EFFECTS = {
        ('happy', 'Vylepšení'),
        ('sad', 'Postih'),
        }

class Room(models.Model):
    room_name = models.CharField(max_length=200, null=True)
    actual_player = models.IntegerField(default=0)
    number_of_players = models.IntegerField(default=0)
    
    game_starting_money = models.IntegerField(null=True, blank=True, default=2000)
    
    def __str__(self):        
        return self.room_name
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'



class Player(models.Model):
    
    account = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    joined_room_at = models.DateTimeField(null=True)
    last_notification_read = models.IntegerField(null=True, default=0)
    
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
    is_room_admin = models.BooleanField(default=False)
    
    def __str__(self):
       return self.account.username
    
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        
        
class History(models.Model):
    message = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=20, default='dice')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'History Record'
        verbose_name_plural = 'History Records'
        
class Notification(models.Model):
    message = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=20, default='dice')
    reciever = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    
class Effect(models.Model):
    type = models.CharField(max_length=200, null=True, choices=EFFECTS)
    
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    notification_message = models.CharField(max_length=2000, null=True, blank=True)
    history_record_message_p1 = models.CharField(max_length=2000, null=True, blank=True)
    history_record_message_p2 = models.CharField(max_length=2000, null=True, blank=True)
    
    pindex_change_by = models.IntegerField(null=True, default=0)
    pindex_set_to = models.IntegerField(null=True, default=0)
    money_change_by = models.IntegerField(null=True, default=0)
    wait_moves_set_to = models.IntegerField(null=True, default=0)
    
    give_stalin = models.BooleanField(default=False)
    give_propustka = models.BooleanField(default=False)
    give_proverka = models.BooleanField(default=False)
    give_nuzky = models.BooleanField(default=False)
    give_vesta = models.BooleanField(default=False)
    give_plan_zaminovani = models.BooleanField(default=False)
    
    give_everybody = models.IntegerField(null=True, default=0)
    remove_from_everybody = models.IntegerField(null=True, default=0)
    money_change_by_per_player = models.IntegerField(null=True, default=0)
    
    go_to_vezeni = models.BooleanField(default=False)
    go_to_blazinec = models.BooleanField(default=False)
    go_to_start = models.BooleanField(default=False)
    
    def __str__(self):
        return self.notification_message
    
    class Meta:
        verbose_name = 'Efekt'
        verbose_name_plural = 'Efekty'
