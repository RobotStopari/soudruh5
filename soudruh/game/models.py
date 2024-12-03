from django.db import models
from django.contrib.postgres.fields import ArrayField


class Player(models.Model):
    pid = models.AutoField()
    name = models.CharField(max_length=200, null=True)
    #account
    pindex = models.IntegerField(null=True, default=0)
    money = models.IntegerField(null=True, default=0)
    category = models.CharField(max_length=200, null=True, default='Bezpartijní')
    color = models.CharField(max_length=200, null=True)
    cards = ArrayField(models.CharField(max_length=40, blank=True),size=4)
    marcs = models.IntegerField(null=True, default=0)
    wait_moves = models.IntegerField(null=True, default=0)
    looks_like_stalin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    on_move = models.BooleanField(default=False)
    skipped = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    actual_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    game_starting_money = models.IntegerField(null=True, blank=True, default=0)
    room_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    