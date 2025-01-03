from .models import Player, Message

from random import randint

def ResetPlayer(player):
    player.pindex = 0
    player.money = 0
    player.category = '1-BEZ'
    player.marcs = 0
    
    player.looks_like_stalin = False
    player.propustka = False
    player.proverka = False
    player.nuzky = False
    player.vesta = False
    player.plan_zaminovani = False
    
    player.active = True
    player.on_move = False
    player.skipped = 0
    player.wait_moves = 0
    
    player.save()
    
    
def UpdateNumberOfPlayers(room):
    room.number_of_players = Player.objects.filter(room=room).count()
    room.save()
    
    
def NextPlayerOnMove(num_in_room, last_player):
    if last_player < num_in_room:
        return last_player + 1
    else:
        return 1
    
    
def RollDice(max):
    return randint(1, max)


def ChangeTurn(player):
    room = player.room
    player.on_move = False
    player.save()
    
    players_in_room = Player.objects.filter(room=room)
    room.actual_player = NextPlayerOnMove(players_in_room.count(), room.actual_player)
    room.save()
    
    next_player = players_in_room[room.actual_player - 1]
    next_player.on_move = True
    next_player.save()
    
def SendMessage(type, message, player, room):
    new_message = Message(type=type, message=message, reciever=player, room=room)
    new_message.save()