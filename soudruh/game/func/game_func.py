from ..models import *

from random import randint

from ..vars import *

wants_to_senf_effect_message = None
    
def RollDice(max, player, room): # hoď kostkou
    throw = randint(1, max)
    
    if throw == max:
        throw += randint(1, max)
        
        if throw == max * 2:
            throw += randint(1, max)
            
            if throw == max * 3:
                throw += randint(1, max)
                
    AddHistoryRecord(f"{player.account.username.capitalize()} hodil {throw}.", 'dice', room)
    NewNotification(f"Hodil jsi {throw}.", 'dice', player, room)
    
    if throw == max * 4:
        NewNotification(f"Hodil jsi čtyřikrát po sobě {str(max)}. Házíš kostkou vyrobenou na Západě. Jdi do vězení.", 'sad', player, room)
        AddHistoryRecord(f"Soudruh {player.account.username.capitalize()} házel kostkou vyrobenou na Západě a šel do vězení.", 'sad', room)
        SpecialMove(player, 1000, True)
                    
    return throw

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
    
    global wants_to_senf_effect_message
    wants_to_senf_effect_message = se
    
    if se.history_record_message_p1_if_stalin and se.history_record_message_p2_if_stalin:
        AddHistoryRecord(se.history_record_message_p1_if_stalin + ' ' + player.account.username.capitalize() + ' ' + se.history_record_message_p2_if_stalin, type, room)
    else:
        AddHistoryRecord(se.history_record_message_p1 + ' ' + player.account.username.capitalize() + ' ' + se.history_record_message_p2, type, room)
    
    if se.go_to_vezeni:
        SpecialMove(player, 1000, True)
    elif se.go_to_blazinec:
        SpecialMove(player, 1001, True)
    elif se.go_to_start:
        SpecialMove(player, 0, False)
    else:
    
        if se.pindex_change_by:
            player.pindex += se.pindex_change_by
        if se.pindex_set_to:
            player.pindex = se.pindex_change_by
        if se.money_change_by and not se.money_change_by_if_stalin:
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
            
        if se.money_change_by_if_stalin:
            if player.looks_like_stalin:
                player.money += se.money_change_by_if_stalin
            else:
                player.money += se.money_change_by                
    
    player.save()
    return se
    
    
def CheckForSpecialPlaces(pindex, player, room):   
    if pindex in SAD:
        RunEffect(player, room, 'sad')
    elif pindex in HAPPY:
        RunEffect(player, room, 'happy')
    elif pindex in NO_PROVS:
        NewNotification('Neprošel jsi stranickou prověrkou. Vracíš se na start a tvé oběživo ti bylo zabaveno.', 'sad', player, room)
        AddHistoryRecord('Soudruh ' + player.account.username.capitalize() + ' neprošel stranickou prověrkou. Vrací se na start a jeho oběživo mu bylo zabaveno.', 'sad', room)
        SpecialMove(player, 0, False)
        
    if player.money < 0:
        NewNotification('Z důvodu nedostatečných finančních prostředků jsi byl vrácen na start.', 'sad', player, room)
        AddHistoryRecord('Soudruh ' + player.account.username.capitalize() + ' byl z důvodu nedostatečných finančních prostředků vrácen na start.', 'sad', room)
        SpecialMove(player, 0, False)
        
    if wants_to_senf_effect_message:
        SendEffectMessage(player, room)
        
    player_on_same_pindex = Player.objects.filter(room=room).exclude(id=player.id).filter(pindex=player.pindex)
    
    if player_on_same_pindex.exists() and player.pindex not in [0, 1000, 1001]:
        KickOutPlayer(player_on_same_pindex, player, room)

def SpecialMove(player, index, remove_all):
    player.pindex = index
    player.money = 0
    player.marcs = 0
    player.category = '1-BEZ'
    player.wait_moves = 0
    
    if remove_all:
        player.proverka = False
        player.nuzky = False
        player.vesta = False
        player.plan_zaminovani = False
    
    player.save()
    
def SendEffectMessage(player, room):
    global wants_to_senf_effect_message
    if wants_to_senf_effect_message.notification_message_if_stalin:
        NewNotification(wants_to_senf_effect_message.notification_message_if_stalin, wants_to_senf_effect_message.type, player, room)
    else:
        NewNotification(wants_to_senf_effect_message.notification_message, wants_to_senf_effect_message.type, player, room)
    wants_to_senf_effect_message = None
    
def KickOutPlayer(player_on_same_pindex, player, room):
    the_other_player = player_on_same_pindex.first()
    o_money = the_other_player.money
    money_change = 0
    
    if o_money > KICK_OUT_MONEY:
        o_money -= KICK_OUT_MONEY
        player.money += KICK_OUT_MONEY
        money_change = KICK_OUT_MONEY
    else:
        player.money += o_money
        money_change = o_money
        o_money = 0
    
    player.save()
    the_other_player.save()  
    SpecialMove(the_other_player, 0, False)
    
    NewNotification('Vyhodil jsi soudruha ' + the_other_player.account.username.capitalize() + ' a získal jsi od něj ' + str(money_change) + 'KČS.', 'happy', player, room)
    NewNotification('Byl jsi vyhozen soudruhem ' + player.account.username.capitalize() + ' a odevzdal jsi mu ' + str(money_change) + 'KČS.', 'sad', the_other_player, room)
    AddHistoryRecord('Soudruh ' + player.account.username.capitalize() + ' vyhodil soudruha ' + the_other_player.account.username.capitalize() + ' a získal jsi od něj ' + str(money_change) + 'KČS.', 'sad', room)