from ..models import *

from random import randint

SAD = [7, 16, 21, 33, 45, 55, 70, 73, 81, 101, 120, 145, 165, 170, 205, 254, 275, 289, 305, 310, 347, 356, 394, 395, 397, 398, 399, 430, 432, 434]
HAPPY = [26, 64, 91, 106, 113, 129, 142, 148, 156, 178, 188, 217, 234, 248, 264, 268, 295, 322, 336, 362, 370, 384, 410, 422]
NO_PROVS = [132, 134, 136, 158, 160, 162]
PROVS = [131, 133, 135, 159, 161, 163]
MONEY_PLACES = [15, 29, 43, 56, 72, 86, 100, 115, 128, 143, 172, 186, 201, 215, 230, 244, 259, 273, 288, 303, 317, 332, 346, 361, 376, 390, 405, 419]
MONEY_PLACES_VALUES = [700, 750, 800, 850, 900, 950, 1000, 2500, 3500, 5000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 28000, 32000, 40000, 46000, 50000, 100000, 100000, 100000, 100000, 100000]
    
    
def RollDice(max): # hoď kostkou
    return randint(1, max)

def Notify(type, message, player, room): # ulož do databáze zprávu
    new_notification = Notification(type=type, message=message, reciever=player, room=room)
    new_notification.save()

def AddHistoryRecord(message, type, room): # ulož do databáze history record
    new_record = History(message=message, type=type, room=room)
    new_record.save()
    
def NewNotification(message, type, reciever, room): # ulož do databáze notifikaci
    new_notification = Notification(message=message, type=type, reciever=reciever, room=room)
    new_notification.save()
    
def RunEffect(player, room, type):
    effects = Effect.objects.filter(type=type).filter(category=player.category)
    sel_number = randint(1, effects.count())
    se = effects[sel_number - 1]
    
    players = Player.objects.filter(room=room)
    
    NewNotification(se.notification_message, type, player, room)
    AddHistoryRecord(se.history_record_message_p1 + ' ' + player.account.username.capitalize() + ' ' + se.history_record_message_p2, type, room)
    
    if se.go_to_vezeni:
        Vezeni(player)
    elif se.go_to_blazinec:
        Vezeni(player)
    elif se.go_to_start:
        player.pindex = 0
    else:
    
        if se.pindex_change_by:
            player.pindex += se.pindex_change_by
        if se.pindex_set_to:
            player.pindex = se.pindex_change_by
        if se.money_change_by:
            player.money += se.money_change_by
        if se.wait_moves_set_to:
            player.wait_moves = se.wait_moves_set_to
        
        if se.give_stalin:
            player.looks_like_stalin = True
        if se.give_propustka:
            player.propustka = True
        if se.give_proverka:
            player.proverka = True
        if se.give_nuzky:
            player.nuzky = True
        if se.give_vesta:
            player.vesta = True
        if se.give_plan_zaminovani:
            player.plan_zaminovani = True
        
        if se.give_everybody:
            for pl in players:
                if pl != player:
                    pl.money += se.give_everybody
                    pl.save()
        if se.remove_from_everybody:
            for pl in players:
                if pl != player:
                    pl.money -= se.give_everybody
                    pl.save()
        if se.money_change_by_per_player:
            player.money += se.money_change_by_per_player * players.count()
    
    player.save()
    
    
def CheckForSpecialPlaces(pindex, player, room):
    if pindex in SAD:
        RunEffect(player, room, 'sad')
    elif pindex in HAPPY:
        RunEffect(player, room, 'happy')
        

def Vezeni(player):
    return

def Blazinec(player):
    return