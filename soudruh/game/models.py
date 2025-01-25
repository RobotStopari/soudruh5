from django.db import models
from django.contrib.auth.models import User

from colorfield.fields import ColorField

from .vars import *

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
    heading_from = models.IntegerField(null=True, default=0)
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
    type = models.CharField(max_length=200, null=True, choices=EFFECTS, help_text="postih nebo vylepšení")
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES, help_text="pro jakou kategorii se využije")
    
    notification_message = models.CharField(max_length=2000, null=True, help_text="oznámení, které uživateli přijde")
    history_record_message_p1 = models.CharField(max_length=2000, null=True, help_text="první část zprávy v herním deníku, po ní bude automaticky přidána mezera, jméno hráče a mezera")
    history_record_message_p2 = models.CharField(max_length=2000, null=True, help_text="druhá část zprávy v herním deníku, před ní je jméno hráče a mezera automaticky")
    
    pindex_change_by = models.IntegerField(null=True, blank=True, default=0, help_text="o kolik se změní políčko hráče (záporné číslo dozadu)")
    pindex_set_to = models.IntegerField(null=True, blank=True, default=0, help_text="na jaké políčko je hráč přesunut (nelze použít políčka 0, 1000 a 1001)")
    money_change_by = models.IntegerField(null=True, blank=True, default=0, help_text="o kolik se změní peníze hráče (záporné číslo odečte)")
    wait_moves_set_to = models.IntegerField(null=True, blank=True, default=0, help_text="kolik kol hráč nehraje (je přeskočen)")
    
    give_stalin = models.BooleanField(default=False, help_text="hráč odteď po zbytek hry vypadá jako Stalin")
    give_propustka = models.BooleanField(default=False, help_text="hráč získá propustku z vězení")
    give_proverka = models.BooleanField(default=False, help_text="hráč získá jednu automaticky splněnou stranickou prověrku")
    give_nuzky = models.BooleanField(default=False, help_text="hráč získá nůžky na ostnatý drát")
    give_vesta = models.BooleanField(default=False, help_text="hráč získá neprůstřelnou vestu")
    give_plan_zaminovani = models.BooleanField(default=False, help_text="hráč získá plán zaminování")
    
    give_everybody = models.IntegerField(null=True, blank=True, default=0, help_text="množství peněz, které se přidají každému hráči, krom tohoto (kladné číslo)")
    remove_from_everybody = models.IntegerField(null=True, blank=True, default=0, help_text="množství peněz, které se odečte každému hráči, krom tohoto (kladné číslo)")
    money_change_by_per_player = models.IntegerField(null=True, blank=True, default=0, help_text="množství peněz, kteté získá tento hráč za každého dalšího hráče v místnosti (záporné číslo je odečte)")
    
    go_to_vezeni = models.BooleanField(default=False, help_text="pošle hráče rovnou do vězení a ztratí vešekeré oběživo")
    go_to_blazinec = models.BooleanField(default=False, help_text="pošle hráče rovnou do blázince a ztratí veškeré oběživo")
    go_to_start = models.BooleanField(default=False, help_text="pošle hráče na start ale neztratí oběživo")
    
    money_change_by_if_stalin = models.IntegerField(null=True, blank=True, help_text="pokud je vyplněno a pokud hráč vypadá jako Stalin, nezíská money_change by (musí být vyplněno), ale tyto peníze (záporné číslo je odečte)")
    notification_message_if_stalin = models.CharField(max_length=2000, null=True, blank=True, help_text="pokud je vyplněno a pokud hráč vypadá jako Stalin, není zobrazena běžná notifikace (musí být vyplněna), ale tato")
    history_record_message_p1_if_stalin = models.CharField(max_length=2000, null=True, blank=True, help_text="pokud je vyplněno a pokud hráč vypadá jako Stalin, není použita první polovina zprávy v herním deníku (musí být vyplněna), ale tato")
    history_record_message_p2_if_stalin = models.CharField(max_length=2000, null=True, blank=True, help_text="pokud je vyplněno a pokud hráč vypadá jako Stalin, není použita druhá polovina zprávy v herním deníku (musí být vyplněna), ale tato")
    
    def __str__(self):
        return self.notification_message
    
    class Meta:
        verbose_name = 'Efekt'
        verbose_name_plural = 'Efekty'

class ChatMessage(models.Model):
    message = models.CharField(max_length=2000, null=True)
    author = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Zpráva v chatu'
        verbose_name_plural = 'Zprávy v chatu'