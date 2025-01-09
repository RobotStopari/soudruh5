from ..models import *

from random import randint

from ..vars import *
    
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